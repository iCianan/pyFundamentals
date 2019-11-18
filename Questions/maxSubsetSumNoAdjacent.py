# Write a function that takes in an array of positive integers
# representing the max sum of non-adjacent elements in the array.
# If a sum cannot be generated, return 0


def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = {}
    maxSums[0] = array[0]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    return max(maxSums.values())


def maxSubsetSumNoAdjacentPro(array):
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    return maxSums[-1]


def main():
    nums = [4, 3, 5, 200, 5, 3]
    print(maxSubsetSumNoAdjacent(nums))
    print(maxSubsetSumNoAdjacentPro(nums))


if __name__ == "__main__":
    main()
