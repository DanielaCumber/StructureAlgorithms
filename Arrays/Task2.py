# How do you find the duplicate number on a given integer array?

import numpy as np

# create random number generator

np.random.seed(0)

# Create an array with 100 random integers from 1 to 100
random_array = np.random.randint(1, 101, size=100)

print(random_array)


def find_duplicate(random_array):  # define a function with the argument "random_array".
    seen_integers = set()  # create an empty set to store the seen numbers
    duplicates = set()  # an empty list to store duplicate numbers.
    for num in random_array:  # starts a loop that will iterate through each number in the array
        if num in seen_integers:  # Within the loop, check if the current number is already in the set.

            duplicates.add(num)  # Add the number to the set
        else:
            seen_integers.add(num)  # If the number is already in the set, it's a duplicate

    return duplicates


# Example usage:
print(find_duplicate(random_array))  # Prints the duplicate number


vals, cnts = np.unique(random_array, return_counts=True)
print(vals[cnts > 1], cnts[cnts > 1])

