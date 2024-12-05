import re
import sys


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

total = 0
for update in updates:
    update = update.split(',')
    update_pages = [int(string) for string in update]
    correct = True
    for rule in rules:
        if rule[0] in update_pages and rule[1] in update_pages and update_pages.index(rule[0]) > update_pages.index(rule[1]):
            correct = False
            break
    if correct:
        middle = update_pages[len(update_pages) // 2]
        total += middle

print(total)
