def moveZeroes(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] == 0:
                swap(nums, j, j+1)
    return nums


def swap(array, left, right):
    if right < len(array):
        array[left], array[right] = array[right], array[left]


def moveZeroesMaster(nums):
    for i in range(len(nums)):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
    for i in range(len(nums)):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)


def main():
    nums = [0, 0, 1]
    print(moveZeroesMaster(nums))


if __name__ == "__main__":
    main()
