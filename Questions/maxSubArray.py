def maxSubArray(nums: 'List[int]') -> 'int':
    maxSoFar = nums[0]
    maxEndingHere = nums[0]
    for i in range(1, len(nums)):
        maxEndingHere = max(maxEndingHere + nums[i], nums[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar


def maxSubArrayNaive(nums: 'List[int]') -> 'int':
    max_sum = float('-inf')
    for left in range(len(nums)):
        current = 0
        for right in range(left, len(nums)):
            current += nums[right]
            max_sum = max(max_sum, current)
    return max_sum


def main():
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArrayNaive([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    main()
