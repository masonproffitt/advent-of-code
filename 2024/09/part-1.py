import sys


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.read().strip()

lengths = [int(x) for x in text]

last_file_id = -1
block_file_ids = []
for i in range(len(lengths)):
    if i % 2 == 0:
        new_file_id = last_file_id + 1
        block_file_ids += [new_file_id] * lengths[i]
        last_file_id = new_file_id
    else:
        block_file_ids += [-1] * lengths[i]

checksum = 0
for i in range(len(block_file_ids)):
    if block_file_ids[i] == -1:
        for j in range(len(block_file_ids) - 1, -1, -1):
            if block_file_ids[j] != -1:
                last_file_block_index = j
                break
        if last_file_block_index <= i:
            break
        block_file_ids[i] = block_file_ids[last_file_block_index]
        block_file_ids[last_file_block_index] = -1
    checksum += i * block_file_ids[i]

print(checksum)
