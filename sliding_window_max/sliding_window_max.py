'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

def sliding_window_max(nums: list, k):
    # Your code here
    # so basically
    # grab k elements and iterate through length of nums - k size
    # ex length = 8, size = 3, so iterate 5 times
    # when we grab k elements, find max and append to new array
    largest = []
    max_value_in_segment = float('-inf')
    index_max_value = 0
    # grabs k elements initially
    segment = nums[:k]
    for iteration in range(len(nums) - k + 1):

        if iteration > 0:
            segment.pop(0) # get rid of first element
            index_max_value -= 1
            segment.append(nums[iteration + k - 1])
            if index_max_value < 0:
                max_value_in_segment = max(segment)
                index_max_value = segment.index(max_value_in_segment)
            # compare current max with newest addition
            if max_value_in_segment < segment[-1]:
                max_value_in_segment = segment[-1]
                index_max_value = len(segment) - 1
            largest.append(max_value_in_segment)
        else:
        # this should run only once and is set up for max_value
            max_value_in_segment = max(segment)
            index_max_value = segment.index(max_value_in_segment)
            largest.append(max_value_in_segment)
    return largest

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
