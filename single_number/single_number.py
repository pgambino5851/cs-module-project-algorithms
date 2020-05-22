'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    count = 1
    num = arr[0]
    
    for i in arr[1:]:
        print(f"i is: {i}")
        if i == num and count == 1:
            print(f"i is: {i} and num is {num}")
            count = 0
        elif i is not num and count == 0:
            num = i
            count += 1
            
    return num

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

