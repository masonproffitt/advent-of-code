import re
import sys


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.read()

pattern = r'^(.+) +(.+)$'
search_results = re.findall(pattern, text, re.MULTILINE)

left = list()
right = list()

for pair in search_results:
    left.append(int(pair[0]))
    right.append(int(pair[1]))

left.sort()
right.sort()

distance = 0

for pair in zip(left, right):
    pair_distance = abs(pair[0] - pair[1])
    distance += pair_distance

print(distance)
