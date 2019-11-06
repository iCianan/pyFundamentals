# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order.
# If no two numbers sum up to the target sum, the function should return an empty array.
# Assume that there will be at most one pair of numbers summing up to the target sum.

# Input [3,5,-4,8,11,1,-1,6] 10
# Output [-1,11]


def twoNumberSum(array, sum):
    cache = {}
    for num in array:
        potentialMatch = sum - num
        if potentialMatch in cache:
            return sorted([potentialMatch, num])
        else:
            cache[num] = True
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
sum = 10

print(twoNumberSum(array, sum))
