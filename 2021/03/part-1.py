import sys

import numpy as np

array = np.genfromtxt(sys.stdin, delimiter=1).T

gamma_rate_digits = []
epsilon_rate_digits = []
for bit_position in array:
    most_common_value = round(bit_position.mean())
    gamma_rate_digits.append(most_common_value)
    epsilon_rate_digits.append(1 - most_common_value)

gamma_rate = int(''.join(str(digit) for digit in gamma_rate_digits), 2)
epsilon_rate = int(''.join(str(digit) for digit in epsilon_rate_digits), 2)

print(f'{gamma_rate} * {epsilon_rate} = {gamma_rate * epsilon_rate}')
