import re
import sys


comparison_string = 'MAS'
def check_string(string):
    return string == comparison_string or string[::-1] == comparison_string


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.readlines()
for i in range(len(text)):
    text[i] = text[i].strip()

ur_coords = set()

for ur_diagonal_index in range(len(comparison_string) - 1, len(text) + len(text[-1]) - len(comparison_string)):
    if ur_diagonal_index < len(text):
        row_index = ur_diagonal_index
        column_index = 0
    else:
        row_index = len(text) - 1
        column_index = ur_diagonal_index - len(text) + 1
    for i in range(min(row_index - (len(comparison_string) - 2), len(text[-1]) - column_index - (len(comparison_string) - 1))):
        string = ''.join([text[row_index - (i + j)][column_index + (i + j)] for j in range(len(comparison_string))])
        if check_string(string):
            ur_coords.add((row_index - (i + 1), column_index + i + 1))

ul_coords = set()

for ul_diagonal_index in range(len(comparison_string) - 1, len(text) + len(text[-1]) - len(comparison_string)):
    if ul_diagonal_index < len(text[-1]):
        row_index = len(text) - 1
        column_index = ul_diagonal_index
    else:
        row_index = len(text) - (ul_diagonal_index - len(text[-1])) - (len(comparison_string) - 2)
        column_index = len(text[-1]) - 1
    for i in range(min(column_index - (len(comparison_string) - 2), row_index - (len(comparison_string) - 2))):
        string = ''.join([text[row_index - (i + j)][column_index - (i + j)] for j in range(len(comparison_string))])
        if check_string(string):
            ul_coords.add((row_index - (i + 1), column_index - (i + 1)))

print(len(ur_coords.intersection(ul_coords)))
