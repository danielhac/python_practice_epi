# Write a program that takes an array A and an index i into A, 
# and rearranges the elements such that all elements less than 
# A[i] (the "pivot") appear first, followed by elements equal to the pivot, 
# followed by elements greater than the pivot.


# During each iteration, the current elem does not increment (move right) until cur <= pivot value
# Meanwhile, when cur > pivot, cur and more elem are swapped, and 'more' is decremented (move left)
def dutch_flag_sort(arr, pivot):
    less = 0
    cur = 0
    more = len(arr)

    while cur < more:
        if arr[cur] < pivot:
            arr[less], arr[cur] = arr[cur], arr[less]
            less, cur = less + 1, cur + 1
        elif arr[cur] > pivot:
            more -= 1
            arr[cur], arr[more] = arr[more], arr[cur]
        else:
            cur += 1
            

    print(arr)   


# Instructions: run 3 times, with a each 'pivot' 
arr = [0,1,2,0,2,1,1]
pivot = arr[0]
# pivot = arr[1]
# pivot = arr[2]
dutch_flag_sort(arr, pivot)
