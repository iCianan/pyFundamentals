class Stack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, value):
        newMinMax = {'min': value, 'max': value}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[-1]
            newMinMax["min"] = min(lastMinMax["min"], value)
            newMinMax["max"] = max(lastMinMax["max"], value)
        self.minMaxStack.append(newMinMax)
        self.stack.append(value)

    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]


def main():
    stack = Stack()
    stack.push(9)
    stack.push(2)
    stack.push(9)
    stack.push(14)
    stack.push(12)
    print(stack.peek())
    print(stack.getMax())
    print(stack.getMin())


if __name__ == "__main__":
    main()
