# How do you find the largest and smallest number in an unsorted integer array?
# Data generator
import numpy as np

np.random.seed(0)
original_array = np.arange(1, 101)
np.random.shuffle(original_array)

Function find_min_max(numbers)
    Set min_num and max_num on the first number of numbers
    For each number in numbers from the second number onwards
        If the number is less than num_min
            Set num_min to the number
        If the number is greater than max_num
            Set max_num to the number
    Returns min_num and max_num
End of function

Generate an array of numbers from 1 to 100 and shuffle it to get original_array

Call find_min_max with original_array and store results in min_num and max_num

Print min_num and max_num


def numbers


