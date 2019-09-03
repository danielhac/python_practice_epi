# This problem is motivated by the need for a company to select a 
# random subset of its customers to roll out a new feature to. 
# For example, a social networking company may want to see the effect of a 
# new UI on page visit duration without taking the chance of alienating 
# all its users if the rollout is unsuccessful.

# Implement an algorithm that takes as input an array of distinct elements 
# and a size, and returns a subset of the given size of the array elements. 
# All subsets should be equally likely. Retum the result in input array itself.


import random

# O(n) time
# Loop through k (size) and get a random elem btwn cur elem and lenth of arr,
# swap cur elem with the random elem.
def random_sampling(k, arr):
    for i in range(k):
        r = random.randint(i, len(arr) - 1)
        arr[i], arr[r] = arr[r], arr[i]
    
    print(arr)


k = 2
arr = [3,7,5,11]
random_sampling(k, arr)