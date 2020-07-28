'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums, k):
    # Your code here
    # so basically
    # grab k elements and iterate through length of nums - k size
    # ex length = 8, size = 3, so iterate 5 times
    # when we grab k elements, find max and append to new array
    largest = []
    for iteration in range(len(nums) - k + 1):
        # grab k elements
        segment = set(nums[iteration:iteration+k])
        largest.append(max(segment))

    return largest

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
