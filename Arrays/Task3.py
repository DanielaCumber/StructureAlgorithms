# How do you find the largest and smallest number in an unsorted integer array?
# Data generator

import numpy as np

np.random.seed(1)
original_array = np.arange(1, 101)
np.random.shuffle(original_array)

def find_min_and_max(numbers):  # Define la función que toma una lista de números

    # minimum_number = min(numbers)
    # max_num = max(numbers)
    # return minimum_number, max_num

    min_number = max_number = numbers[0]  # is a form of multiple assignment in Python. the assignment is made from right to left
    for num in numbers[1:]:  # iterates over all the elements of the Numbers list, starting from the second element (index 1) to the end. The notation numbers[1:] means "all elements of numbers from index 1 to the end".
        if num < min_number:  # Inside the loop, this line checks if the current element "num" is less than the value stored in min_val.
            min_number = num  # If "num" is smaller than min_val, then min_val is updated to be "num". This ensures that min_val always contains the smallest value found so far in the list.
        if num > max_number:  # If "num" is not less than min_val, this line checks if "num" is greater than the value stored in max_val.
            max_number = num  # If "num" is greater than max_val, then max_val is updated to be "num". This ensures that max_val always contains the largest value found so far in the list.

    return min_number, max_number

min_val, max_val = find_min_and_max(original_array)  # These are two variables used to store the values returned by the min_and_max function. This is the call to the min_and_max function with the original array_array as argument
print(f"Valor mínimo: {min_val}, Valor máximo: {max_val}")

