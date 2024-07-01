# How do you find the missing numbers in a given integer array of 1 to 100?
# Data generator
import numpy as np

np.random.seed(0)
original_array = np.arange(1, 101)
np.random.shuffle(original_array)
mod_array = np.delete(original_array, [50, 10, 20, 30])

# code
expected = set(range(1, 101))  # create a set

actual = set(mod_array)  # Converts mod_array to a set

missing_numbers = expected - actual  # missing numbers are in Expected but not in Actual

print(f'{missing_numbers}')
print(original_array[50], original_array[10], original_array[20], original_array[30])
