import re
import sys


def check_correctness(rules, update):
    correct = True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            left_pos = update.index(rule[0])
            right_pos = update.index(rule[1])
            if left_pos > right_pos:
                correct = False
                break
    return correct


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.read()

section_divider_index = text.find('\n\n')

section_one, section_two = text[:section_divider_index], text[section_divider_index:]

rules = re.findall(r'^(\d+)\|(\d+)$', section_one, re.MULTILINE)
for i in range(len(rules)):
    rules[i] = [int(rules[i][0]), int(rules[i][1])]

updates = re.findall(r'^(?:\d+(?:,|$))+', section_two, re.MULTILINE)
for i in range(len(updates)):
    update = updates[i]
    update = update.split(',')
    updates[i] = [int(string) for string in update]

total = 0
for i in range(len(updates)):
    if not check_correctness(rules, updates[i]):
        correct = False
        while not correct:
            for rule in rules:
                if rule[0] in updates[i] and rule[1] in updates[i]:
                    left_pos = updates[i].index(rule[0])
                    right_pos = updates[i].index(rule[1])
                    if left_pos > right_pos:
                        correct = False
                        tmp = updates[i][left_pos]
                        updates[i][left_pos] = updates[i][right_pos]
                        updates[i][right_pos] = tmp
            correct = check_correctness(rules, updates[i])
        middle = updates[i][len(updates[i]) // 2]
        total += middle

print(total)
