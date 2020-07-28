'''
Input: a List of integers
Returns: a List of integers
'''
from functools import reduce

def partition_list_without_i(arr, i):
    return arr[:i] + arr[i+1:]

def product_of_all_other_numbers(arr):
    # Your code here
    # given an item at index you would multiply that item by all other items
    new_list = []
    for i in range(len(arr)):
        # grab the beginning up to i [:i] i being exclusive
        # grab from i + 1 to end
        # reduce by multiplying
        other_numbers_array = partition_list_without_i(arr, i)
        reduced_product = reduce(lambda prev, next_value: prev * next_value, other_numbers_array)
        new_list.append(reduced_product)
    return new_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
