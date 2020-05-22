'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    resArr = []
    windowArr = []
    index = 0
    for i in range(len(arr)):
        windowArr = []
        index = i
        while(len(windowArr) is not k):
            print(f"index is: {index}")
            windowArr.append(nums[index])
            index += 1
        resArr.append(max(windowArr))
        if windowArr[len(windowArr) - 1] is nums[len(nums) - 1]:
            break


    return resArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
