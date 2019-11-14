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
        if array[i] in maxSums:
            return maxSums[i]
        else:
            maxSums[i] = max(maxSums[i-1], maxSums[i-2] + array[i])
    return max(maxSums.values())


def main():
    nums = [75, 105, 120, 75, 90, 135]
    print(maxSubsetSumNoAdjacent(nums))


if __name__ == "__main__":
    main()
