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


def get_fence_sections(types, plot):
    fence_sections = []
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
                fence_sections.append(((i, j), (step[0] - i, step[1] - j)))

    return fence_sections


def get_n_sides(fence_sections):
    n_sides = 0
    remaining_fence_sections = list(fence_sections)
    while len(remaining_fence_sections) > 0:
        fs = remaining_fence_sections[0]
        if fs[1][0] == 0:
            step = [1, 0]
        else:
            step = [0, 1]
        n = 1
        while True:
            next_fs = ((fs[0][0] + n * step[0], fs[0][1] + n * step[1]), fs[1])
            if next_fs in remaining_fence_sections[1:]:
                remaining_fence_sections.remove(next_fs)
                n += 1
            else:
                break
        n = -1
        while True:
            next_fs = ((fs[0][0] + n * step[0], fs[0][1] + n * step[1]), fs[1])
            if next_fs in remaining_fence_sections[1:]:
                remaining_fence_sections.remove(next_fs)
                n -= 1
            else:
                break
        remaining_fence_sections.remove(fs)
        n_sides += 1

    return n_sides


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
    fence_sections = get_fence_sections(types, plot)
    n_sides = get_n_sides(fence_sections)
    price += area * n_sides

print(price)
