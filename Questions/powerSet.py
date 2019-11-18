def powerSet(array):
    subsets = [[]]
    for num in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [num])
    return subsets

def powerSetR(array, i=None):
    if i is None:
        i = len(array) -1
    if i < 0:
        return [[]]
    num = array[i]
    subsets = powerSetR(array, i - 1)
    for i in range(len(subsets)):
        current = subsets[i]
        subsets.append(current + [num])
    return subsets

def main():
    sub = [1,2]
    print(powerSetR(sub))


if __name__ == "__main__":
    main()
