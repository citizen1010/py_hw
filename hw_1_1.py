"""

Permutation function
"""
from itertools import permutations


def permute(n):
    if n == 1:
        print(n)
    elif 2 <= n <= 7:
        sorted_array = create_sort_array(n)
        result_array = permute_array(sorted_array)
        print_permutation_elements(result_array)
    else:
        print("Error: 1 <= n <= 7")


def create_sort_array(n):
    array = []
    while n > 0:
        array.append(n)
        n = n - 1
    array.sort()
    return array


def permute_array(sorted_array):
    new_array = []
    for i in permutations(sorted_array):
        new_array.append(i)
    new_array = list(map(list, new_array))  # converting list of tuples to list of lists
    return new_array


def print_permutation_elements(result_array):
    for element in result_array:
        print(' '.join(map(str, element)), end='\n')  # printing without brackets and commas


print("Result for 'n' = 1:")
permute(1)
print("Result for 'n' > 7:")
permute(9)
print("Result for 'n' => 2  and 'n' <= 7:")
permute(5)

