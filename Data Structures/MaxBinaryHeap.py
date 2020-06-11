import math


class MaxBinaryHeap:
    def __init__(self):
        self.value = []

    def Insert(self, value):
        self.value.append(value)
        self.BubbleUp()

    def BubbleUp(self):
        index = len(self.value) - 1
        if index <= 1:
            return
        parentIndex = math.floor((index - 1) / 2)
        while parentIndex > -1 and self.value[parentIndex] < self.value[index]:
            self.swap(self.value, parentIndex, index)
            index = parentIndex
            parentIndex = math.floor((index - 1) / 2)

    def swap(self, array, i, j):
        array[i], array[j] = array[j], array[i]


def main():
    heap = MaxBinaryHeap()
    heap.Insert(55)
    heap.Insert(32)
    heap.Insert(20)
    heap.Insert(8)
    heap.Insert(15)
    heap.Insert(9)
    heap.Insert(174)
    heap.Insert(3)
    heap.Insert(5465)

    print(heap.value)


if __name__ == "__main__":
    main()
