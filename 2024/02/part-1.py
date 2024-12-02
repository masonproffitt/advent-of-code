import sys

import numpy as np


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

n_safe = 0
for line in text_source.readlines():
    a = np.fromstring(line, sep=' ')
    diff = np.diff(a)
    safe = ((diff > 0).all() | (diff < 0).all()) & ((abs(diff) >= 1) & (abs(diff) <= 3)).all()
    n_safe += safe

print(n_safe)
