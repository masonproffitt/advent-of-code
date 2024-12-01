import re
import sys

import numpy as np


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

left = np.array(left)
right = np.array(right)

score = 0

for entry in left:
    score += entry * (right == entry).sum()

print(score)
