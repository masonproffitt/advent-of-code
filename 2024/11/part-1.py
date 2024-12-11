import sys


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.read()

stone_strings = text.split(' ')
stones = [int(s) for s in stone_strings]

n_blinks = 0
while n_blinks < 25:
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
            i += 1
            continue
        stone_string = str(stones[i])
        string_length = len(stone_string)
        if string_length % 2 == 0:
            stones[i] = int(stone_string[:string_length // 2])
            stones.insert(i + 1, int(stone_string[string_length // 2:]))
            i += 2
            continue
        stones[i] *= 2024
        i += 1
    n_blinks += 1

print(len(stones))
