# Implementation of Merge Sort
# Intuition : 
#   We need to divide the array we get into a singular arrays by cutting it down in the mid so we have a sorted array
#   And, then we need to pass it to the function which will take in two sorted arrays (intial array lenght of one) and then merge them in sorted order
#   And, we return the entrie array

# Pass in sorted arrays
def merge(arr1, arr2):
    left_ptr = 0
    right_ptr = 0

    new_arr = []

    # Merge the two sorted arrays in a sorted way using two pointers
    while left_ptr < len(arr1) and right_ptr < len (arr2):
        if arr1[left_ptr] <= arr2[right_ptr]:
            new_arr.append(arr1[left_ptr])
            left_ptr+=1
            # Increasing left ptr to see if the next element is bigger than the other one
        else:
            new_arr.append(arr2[right_ptr])
            right_ptr +=1

    # If loop is exited and left pointer is still less than len of arr, add the remaning elements to the arr
    if left_ptr < len(arr1):
        for x in range(left_ptr, len(arr1)):
            new_arr.append(arr1[x])
    
    # If loop is exited but elements in arr2, add them to arr
    elif right_ptr < len(arr2):
        for x in range(right_ptr, len(arr2)):
            new_arr.append(arr2[x])

    return new_arr

# Merge sort function
# Takes in an arr
# Initially it is going to be the unsorted array
def merge_sort(arr):
    # Base case
    # When len of arr is 1 or less than 2, return the arr because single element array is sorted in itself
    if len(arr) < 2:
        return arr

    # Split the arr into two halves
    mid = len(arr)//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # Now, since we have two arrays, perform the recurisve call on these arrays
    return merge(merge_sort(left_arr), merge_sort(right_arr))

# Taking in the user input
user_input = input("Enter the unsorted array in the format of [1,2,3] etc.. : ")
user_input = user_input[1:-1]
user_input_list = list(map(int, user_input.split(",")))

print(merge_sort(user_input_list))