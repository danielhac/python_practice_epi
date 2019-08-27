# Your input is an array of integers, 
# and you have to reorder its entries so that the even entries appear first. 
# This is easy if you use O(n) space, where n is the length of the array. 
# However, you are required to solve it without allocating additional storage.


# Set up subarrays (within same array):
#   even:   starting at idx 0
#   odd:    starting and last idx
# 
# Loop until even subarray meets odd
def even_odd(arr):
    next_even = 0
    next_odd = len(arr) - 1

    # If elem is even, move idx up 1, else swap the cur elem with 'next_odd' elem
    # If swapped, the new cur elem is checked
    while next_even < next_odd:
        # even
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            # odd - swap - NOTE: when set up like below, no temp needed
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1


    return arr

print(even_odd([1,2,3,4,5,6,7,8,9]))