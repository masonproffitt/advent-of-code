import sys
import math


def is_valid_location(location, n_rows, n_columns):
    return location[0] >= 0 and location[1] >= 0 and location[0] < n_rows and location[1] < n_columns


def add_n_times(v1, v2, n):
    return v1[0] + n * v2[0], v1[1] + n * v2[1]


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
            antinodes.add(antennas[i])
            difference = (antennas[i][0] - antennas[j][0], antennas[i][1] - antennas[j][1])
            gcd = math.gcd(*difference)
            delta = (difference[0] // gcd, difference[1] // gcd)
            n = 1
            antinode = add_n_times(antennas[i], delta, n)
            while is_valid_location(antinode, n_rows, n_columns):
                antinodes.add(antinode)
                n += 1
                antinode = add_n_times(antennas[i], delta, n)
            n = -1
            antinode = add_n_times(antennas[i], delta, n)
            while is_valid_location(antinode, n_rows, n_columns):
                antinodes.add(antinode)
                n -= 1
                antinode = add_n_times(antennas[i], delta, n)

print(len(antinodes))
