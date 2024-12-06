import sys

import numpy as np


up = np.array([-1, 0])
down = np.array([1, 0])
left = np.array([0, -1])
right = np.array([0, 1])


def turn_right(direction):
    if (direction == up).all():
        return right
    elif (direction == right).all():
        return down
    elif (direction == down).all():
        return left
    elif (direction == left).all():
        return up


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

lines = text_source.readlines()

n_rows = len(lines)
n_columns = len(lines[0]) - 1

start_position = None
start_direction = None
obstacles = set()
for row_index in range(n_rows):
    line = lines[row_index].strip()
    last = -1
    if start_position is None:
        start_column = line.find('^')
        if start_column > -1:
            start_position = np.array([row_index, start_column])
            start_direction = up
    while True:
        new = line.find('#', last + 1)
        if new == -1:
            break
        else:
            obstacles.add((row_index, new))
            last = new

current_position = start_position
traversed_positions = {tuple(current_position)}
current_direction = start_direction

while True:
    next_step = current_position + current_direction
    if tuple(next_step) in obstacles:
        current_direction = turn_right(current_direction)
        continue
    elif next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= n_rows or next_step[1] >= n_columns:
        break
    else:
        current_position = next_step
        traversed_positions.add(tuple(current_position))

print(len(traversed_positions))
