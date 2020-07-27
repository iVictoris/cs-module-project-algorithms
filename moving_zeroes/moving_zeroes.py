'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr: list):
    # Your code here
    # I'd probably use a linked list here but iterate through list and add to tail or just use list methods
    start = 0
    popped = 0
    while start + popped != len(arr):
        if arr[start] == 0:
            arr.append(arr.pop(start))
            popped += 1
        else:
            start += 1

    return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")