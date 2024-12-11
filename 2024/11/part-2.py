import functools
import math
import sys


@functools.cache
def blink_stone(stone, n_blinks):
    n_blinks_remaining = n_blinks
    while n_blinks_remaining > 0:
        if stone == 0:
            stone = 1
            n_blinks_remaining -= 1
            continue
        string_length = math.floor(math.log10(stone)) + 1
        if string_length % 2 == 0:
            divisor = 10 ** (string_length // 2)
            left = stone // divisor
            right = stone % divisor
            n_blinks_remaining -= 1
            return blink_stone(left, n_blinks_remaining) + blink_stone(right, n_blinks_remaining)
        stone *= 2024
        n_blinks_remaining -= 1

    return 1


def blink_stones(stones, n_blinks):
    results = [blink_stone(stone, n_blinks) for stone in stones]
    return sum(results)


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.read()

stone_strings = text.split(' ')
stones = [int(s) for s in stone_strings]

print(blink_stones(stones, 75))
