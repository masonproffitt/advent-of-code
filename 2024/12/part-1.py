import sys


def get_connections(types, connections, i, j):
    if connections[i][j] is None:
        possible_steps = [
            [i - 1, j],
            [i + 1, j],
            [i, j - 1],
            [i, j + 1],
        ]
        connections[i][j] = {(i, j)}
        for step in possible_steps:
            if (
                step[0] >= 0
                and step[1] >= 0
                and step[0] < len(types)
                and step[1] < len(types[0])
                and types[step[0]][step[1]] == types[i][j]
            ):
                connections = get_connections(types, connections, step[0], step[1])
                connections[i][j] = connections[i][j].union(connections[step[0]][step[1]])

    return connections


def get_perimeter(types, plot):
    perimeter = 0
    for plant in plot:
        i, j = plant
        possible_steps = [
            [i - 1, j],
            [i + 1, j],
            [i, j - 1],
            [i, j + 1],
        ]
        for step in possible_steps:
            if not (
                step[0] >= 0
                and step[1] >= 0
                and step[0] < len(types)
                and step[1] < len(types[0])
                and types[step[0]][step[1]] == types[i][j]
            ):
                perimeter += 1

    return perimeter


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.readlines()

types = []
for line in text:
    types.append([x for x in line.strip()])

n_rows = len(types)
n_columns = len(types[0])

connections = []
for i in range(n_rows):
    connections.append([])
    for j in range(n_columns):
        connections[-1].append(None)

plots = []
for i in range(n_rows):
    for j in range(n_columns):
        if connections[i][j] is None:
            connections = get_connections(types, connections, i, j)
            plots.append(connections[i][j])

price = 0
for plot in plots:
    area = len(plot)
    perimeter = get_perimeter(types, plot)
    price += area * perimeter

print(price)
