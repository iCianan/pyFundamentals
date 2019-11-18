def productSum(numbers):
    results = []
    total = 1
    while len(results) != len(numbers):
            current = numbers[0]
            del numbers[0]
            for num in numbers:
                total *= num
            results.append(total)
            numbers.append(current)
            total = 1
    return results

def productSumMaster(nums):
        p = 1
        n = len(nums)
        output = n * [1]
        for i in range(n):
            output[i] *= p
            p *= nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] *= p
            p *= nums[i]
        return output 


def main():
    nums = [1,2,3,4]
    print(productSumMaster(nums))

if __name__ == "__main__":
    main()

