import sys

import numpy as np


def get_is_safe(a):
    diff = np.diff(a)
    is_safe = ((diff > 0).all() | (diff < 0).all()) & ((abs(diff) >= 1) & (abs(diff) <= 3)).all()
    return is_safe


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

n_safe = 0
for line in text_source.readlines():
    a = np.fromstring(line, sep=' ')

    is_safe = False
    if get_is_safe(a):
        is_safe = True
    else:
        for i in range(0, len(a)):
            modified_a = np.concatenate([a[:i], a[i + 1:]])
            is_safe = get_is_safe(modified_a)
            if is_safe:
                break

    n_safe += is_safe

print(n_safe)
