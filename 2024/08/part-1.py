import sys


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

lines = text_source.readlines()

n_rows = len(lines)
n_columns = len(lines[0].strip())

antenna_dict = {}
for i in range(n_rows):
    for j in range(n_columns):
        char = lines[i][j]
        if char == '.':
            continue
        if char not in antenna_dict:
            antenna_dict[char] = []
        antenna_dict[char].append((i, j))

antinodes = set()
for antenna_type in antenna_dict:
    antennas = antenna_dict[antenna_type]
    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            difference = (antennas[i][0] - antennas[j][0], antennas[i][1] - antennas[j][1])
            pair_antinodes = [
                (antennas[i][0] + difference[0], antennas[i][1] + difference[1]),
                (antennas[j][0] - difference[0], antennas[j][1] - difference[1]),
            ]
            for antinode in pair_antinodes:
                if antinode[0] >= 0 and antinode[1] >= 0 and antinode[0] < n_rows and antinode[1] < n_columns:
                    antinodes.add(antinode)

print(len(antinodes))
