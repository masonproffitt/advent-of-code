# import re
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
permanent_obstacles = set()
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
            permanent_obstacles.add((row_index, new))
            last = new

n_loops = 0
for new_obstacle_row in range(n_rows):
    for new_obstacle_column in range(n_columns):
        new_obstacle_position = (new_obstacle_row, new_obstacle_column)
        if new_obstacle_position in permanent_obstacles or new_obstacle_position == tuple(start_position):
            continue
        obstacles = permanent_obstacles.union({new_obstacle_position})

        current_position = start_position
        current_direction = start_direction
        traversed_states = {(tuple(current_position), tuple(current_direction))}
        while True:
            next_step = current_position + current_direction
            if tuple(next_step) in obstacles:
                current_direction = turn_right(current_direction)
                continue
            elif next_step[0] < 0 or next_step[1] < 0 or next_step[0] >= n_rows or next_step[1] >= n_columns:
                break
            else:
                current_position = next_step
                next_state = (tuple(current_position), tuple(current_direction))
                if next_state in traversed_states:
                    n_loops += 1
                    break
                traversed_states.add(next_state)

print(n_loops)
