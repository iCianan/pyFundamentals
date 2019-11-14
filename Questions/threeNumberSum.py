# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
# If any three numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order.
# If no three numbers sum up to the target sum, the function should return an empty array.

# Input [12,3,1,2,-6,5,-8,6] 0
# Output [[-8,2,6], [-8,3,5], [-6,1,5]]


def threeNumberSum(numbers, targetSum):
    results = []
    numbers.sort()
    for i, num in list(enumerate(numbers)):
        left = i + 1
        right = len(numbers) - 1
        while left < right:
            currentSum = num + numbers[left] + numbers[right]
            if currentSum == targetSum:
                results.append([num, numbers[left], numbers[right]])
                right -= 1
                left += 1
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1
    return results


def main():
    sample = [12, 3, 1, 2, -6, 5, -8, 6]
    sample2 = 0
    print(threeNumberSum(sample, sample2))


if __name__ == "__main__":
    main()
