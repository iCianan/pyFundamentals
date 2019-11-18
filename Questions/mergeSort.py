import math


def MergeSort(numbers):
    if len(numbers) == 1:
        return numbers
    mid = math.floor(len(numbers)/2)
    left = MergeSort(numbers[:mid])
    right = MergeSort(numbers[mid:])
    return Merge(left, right)


def Merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def main():
    nums = [13,4,2,6]
    print(MergeSort(nums))


if __name__ == "__main__":
    main()
