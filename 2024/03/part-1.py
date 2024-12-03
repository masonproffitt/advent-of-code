import re
import sys


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.read()

pattern = r'mul\((\d+),(\d+)\)'
search_results = re.findall(pattern, text)

total = 0
for pair in search_results:
    left = int(pair[0])
    right = int(pair[1])
    total += left * right

print(total)
