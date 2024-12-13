import sys
import re


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.readlines()

a_buttons = []
b_buttons = []
prizes = []
for line in text:
    match = re.search(r'X(?:\+|=)(\d+), Y(?:\+|=)(\d+)$', line)
    if match:
        numbers = [int(x) for x in match.groups()]
    if line.startswith('Button A: '):
        a_buttons.append(numbers)
    elif line.startswith('Button B: '):
        b_buttons.append(numbers)
    elif line.startswith('Prize: '):
        prizes.append(numbers)

a_cost = 3
b_cost = 1

costs = []
for i in range(len(prizes)):
    a_button = a_buttons[i]
    b_button = b_buttons[i]
    prize = prizes[i]

    cost = 0
    max_a = min(prize[0] // a_button[0], prize[1] // a_button[1])
    for n_a in range(max_a + 1):
        remaining_prize = (prize[0] - n_a * a_button[0], prize[1] - n_a * a_button[1])
        n_b = remaining_prize[0] // b_button[0]
        if remaining_prize[0] == n_b * b_button[0] and remaining_prize[1] == n_b * b_button[1]:
            cost = n_a * a_cost + n_b * b_cost

    costs.append(cost)

print(sum(costs))
