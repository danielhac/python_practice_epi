# This problem is concemed with deleting repeated elements from a sorted array. 
# For example, for the array        <2,3,5,5,7,11,11,11,13>, 
# then after deletion, the array is <2,3,5,7,11,13,0,0,0>. 
# After deleting repeated elements, there are 6 valid entries. 
# There are no requirements as to the values stored beyond the last valid element.

# Write a program which takes as input a sorted array and updates it 
# so that all duplicates have been removed and the remaining elements 
# have been shifted left to fill the emptied indices. 
# Return the number of valid elements. 
# Many languages have library functions for performing this operation,
# you cannot use these functions.

# Notes: can prob use some combo of linked list, dictionary 
# but appears that an array needs to be returned.


# Brute force: O(n^2)
# Loop thru array and if arr[i] == arr[i+1], 
#   shift elem left, insert 0 at end of array and
#   reduce length by 1 since we don't need to check for that elem
def delete_dup_sorted_arr(arr):
    valid = 1
    i = 0
    length = len(arr) -1
    while i < length:
        if arr[i] == arr[i+1]:
            j = i
            while j < length:
                arr[j] = arr[j+1]                
                j += 1
            arr[length] = 0
            length -= 1
        else:
            i += 1
            valid += 1

    print(arr)
    print("valid: " + str(valid))



# O(n) solution: 2 passes
# Dictionary used to store values within first loop and then set elem to 0.
#   Now that all elems in arr is set to zero, 
#   loop again to set values in elem from dictionary.
def delete_dup_sorted_arr2(arr):
    dictionary = {}

    for i in range(len(arr)):
        if arr[i] not in dictionary:
            dictionary[arr[i]] = 1
        arr[i] = 0

    j = 0
    for key in dictionary:
        arr[j] = key
        j += 1
    
    print(arr)
    print("valid: " + str(len(dictionary)))


arr = [2,3,5,5,7,11,11,11,13]
# arr = [2,2,2,2]
# arr = [2]

delete_dup_sorted_arr2(arr)