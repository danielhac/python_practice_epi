# Write a program which takes as input an array of digits encoding a 
# nonnegative decimal integer D and updates the array to represent the 
# integer D + 1. 
# For example, if the input is (1,2,9) then you should update the array to (1,3,0). 
# Your algorithm should work even if it is implemented in a language that has finite-precision arithmetic.


# Brute force: convert int elem to string and store in var
#   then convert to int and incr by 1 and store back in arr as int
#   Note: if arr is [9,9] we need another elem
def decimal_arr_brute_force(arr):
    num = "".join(map(str, arr))
    num = str(int(num) + 1)
    
    diff = len(num) - len(arr)
    if diff != 0:
        for j in range(diff):
            arr.append('')

    for k in range(len(num)):
        arr[k] = int(num[k])
    
    print(arr)


# arr = [1,2,9]
#     [1,2,10]
#     [1,3,0]

arr = [9,9]
#     [9,10]
#     [10,0]
#     []
decimal_arr_brute_force(arr)