import sys


def get_connections(heights, connections, i, j):
    if connections[i][j] is None:
        possible_steps = [
            [i - 1, j],
            [i + 1, j],
            [i, j - 1],
            [i, j + 1],
        ]
        connections[i][j] = [(i, j)]
        for step in possible_steps:
            if (
                step[0] >= 0
                and step[1] >= 0
                and step[0] < len(heights)
                and step[1] < len(heights[0])
                and heights[step[0]][step[1]] - heights[i][j] == 1
            ):
                connections = get_connections(heights, connections, step[0], step[1])
                connections[i][j] += connections[step[0]][step[1]]

    return connections


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.readlines()

heights = []
for line in text:
    heights.append([int(x) for x in line.strip()])

n_rows = len(heights)
n_columns = len(heights[0])

connections = []
starts = []
ends = []
for i in range(n_rows):
    connections.append([])
    for j in range(n_columns):
        connections[-1].append(None)
        if heights[i][j] == 0:
            starts.append((i, j))
        elif heights[i][j] == 9:
            ends.append((i, j))

for i in range(n_rows):
    for j in range(n_columns):
        connections = get_connections(heights, connections, i, j)

total = 0
for start in starts:
    for end in ends:
            total += connections[start[0]][start[1]].count(end)

print(total)
