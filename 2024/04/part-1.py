import re
import sys


def check_string(string):
    return string == 'XMAS' or string[::-1] == 'XMAS'


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.readlines()
for i in range(len(text)):
    text[i] = text[i].strip()

total = 0

for row in text:
    for i in range(0, len(row) - 3):
        string = row[i:i+4]
        total += check_string(string)

for column_index in range(len(text[0])):
    column = ''.join([row[column_index] for row in text])
    for i in range(0, len(column) - 3):
        string = column[i:i+4]
        total += check_string(string)

for ur_diagonal_index in range(3, len(text) + len(text[-1]) - 4):
    if ur_diagonal_index < len(text):
        row_index = ur_diagonal_index
        column_index = 0
    else:
        row_index = len(text) - 1
        column_index = ur_diagonal_index - len(text) + 1
    for i in range(min(row_index - 2, len(text[-1]) - column_index - 3)):
        string = ''.join([text[row_index - (i + j)][column_index + (i + j)] for j in range(4)])
        total += check_string(string)

for ul_diagonal_index in range(3, len(text) + len(text[-1]) - 4):
    if ul_diagonal_index < len(text[-1]):
        row_index = len(text) - 1
        column_index = ul_diagonal_index
    else:
        row_index = len(text) - (ul_diagonal_index - len(text[-1])) - 2
        column_index = len(text[-1]) - 1
    for i in range(min(column_index - 2, row_index - 2)):
        string = ''.join([text[row_index - (i + j)][column_index - (i + j)] for j in range(4)])
        total += check_string(string)

print(total)
