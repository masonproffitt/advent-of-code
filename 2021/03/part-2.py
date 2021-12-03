import sys

import numpy as np

def get_most_common_value(a):
    ones = sum(a > 0)
    if ones >= len(a) - ones:
        most_common_value = 1
    else:
        most_common_value = 0
    return most_common_value

array = np.genfromtxt(sys.stdin, dtype=int, delimiter=1)

oxygen_generator_rating_candidates = array.copy()
co2_scrubber_rating_candidates = array.copy()

for bit_position in range(array.shape[1]):
    oxygen_generator_rating_candidates = oxygen_generator_rating_candidates[oxygen_generator_rating_candidates[:, bit_position] == get_most_common_value(oxygen_generator_rating_candidates[:, bit_position])]
    if len(co2_scrubber_rating_candidates) > 1:
        co2_scrubber_rating_candidates = co2_scrubber_rating_candidates[co2_scrubber_rating_candidates[:, bit_position] == 1 - get_most_common_value(co2_scrubber_rating_candidates[:, bit_position])]

oxygen_generator_rating = int(''.join(str(digit) for digit in oxygen_generator_rating_candidates[0]), 2)
co2_scrubber_rating = int(''.join(str(digit) for digit in co2_scrubber_rating_candidates[0]), 2)

print(f'{oxygen_generator_rating} * {co2_scrubber_rating} = {oxygen_generator_rating * co2_scrubber_rating}')
