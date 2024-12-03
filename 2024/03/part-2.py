import re
import sys


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.read()

sections = text.split(sep="don't()")
text = sections[0]
for section in sections[1:]:
    i = section.find('do()')
    if i > -1:
        text += section[i:]

mul_pattern = r'mul\((\d+),(\d+)\)'
search_results = re.findall(mul_pattern, text)

total = 0
for pair in search_results:
    left = int(pair[0])
    right = int(pair[1])
    total += left * right

print(total)
