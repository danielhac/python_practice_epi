# Binary search algo
# Chooses a mid-point within the sorted array,
#   if the searched num, x is less than the mid-point,
#   set the length (right) to mid-1.
# Loop continues and a new mid-point is chosen.
#   If x is more than the mid-point,
#   set the left to mid+1 and loop continues.
# During each iteration, check if the mid-point is x.


def binary_search(arr, left, right, x):
    while left <= right:
        mid = left + (right - left)//2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


arr = [1,2,5,14,22,48,61,79,80,94,99]
x = 94
# x = 93
print(binary_search(arr, 0, len(arr)-1, x))
