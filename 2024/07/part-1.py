import sys


add = (lambda x, y: x + y)
multiply = (lambda x, y: x * y)
ops = [add, multiply]

def is_valid(test_value, operands):
    for op in ops:
        new_operands = [op(operands[0], operands[1])] + operands[2:]
        if len(new_operands) == 1:
            result = new_operands[0] == test_value
            if result:
                break
        else:
            result = is_valid(test_value, new_operands)
            if result:
                break
    return result


if len(sys.argv) > 1:
    text_source = open(sys.argv[1])
else:
    text_source = sys.stdin

lines = text_source.readlines()

total = 0
for line in lines:
    test_value_string, rest = line.split(':')
    test_value = int(test_value_string)
    operands = [int(x) for x in rest.strip().split(' ')]
    result = is_valid(test_value, operands)
    if result:
        total += test_value

print(total)
