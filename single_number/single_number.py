'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

keys = {}

def store(number):
    try:
        keys[number] += 1
    except KeyError:
        keys[number] = 1

def find_single(number_dict):
    # go through keys
    # find key that has value of 1
    # return that key
    for key in number_dict:
        if number_dict[key] == 1:
            return key

def single_number(arr):
    # Your code here
    # the easiest way in my head to do this is to make a dict of numberd and increment the value of the key for each duplicate
    # then go back and see which key has a value of 1
    for item in arr:
        store(item)
    
    return find_single(keys)


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")