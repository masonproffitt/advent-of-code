import sys


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

text = text_source.read().strip()

lengths = [int(x) for x in text]

last_file_id = -1
original_file_block_indices = []
blocks = []
for i in range(len(lengths)):
    if i % 2 == 0:
        new_file_id = last_file_id + 1
        original_file_block_indices.append(len(blocks))
        blocks.append({'size': lengths[i], 'data': [new_file_id] * lengths[i]})
        last_file_id = new_file_id
    else:
        blocks.append({'size': lengths[i], 'data': []})

for origin_block_index in original_file_block_indices[::-1]:
    for destination_block_index in range(origin_block_index):
        free_space = blocks[destination_block_index]['size'] - len(blocks[destination_block_index]['data'])
        if free_space >= blocks[origin_block_index]['size']:
            blocks[destination_block_index]['data'] += blocks[origin_block_index]['data']
            blocks[origin_block_index]['data'] = []
            break

block_file_ids = []
for i in range(len(blocks)):
    block_file_ids += blocks[i]['data']
    block_file_ids += [-1] * (blocks[i]['size'] - len(blocks[i]['data']))

checksum = 0
for i in range(len(block_file_ids)):
    if block_file_ids[i] != -1:
        checksum += i * block_file_ids[i]

print(checksum)
