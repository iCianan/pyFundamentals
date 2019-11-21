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
        if len(self.minMaxStack) > 0:
            newMinMax['min'] = min(value, self.minMaxStack[-1]['min'])
            newMinMax['max'] = max(value, self.minMaxStack[-1]['max'])
        self.minMaxStack.append(newMinMax)
        self.stack.append(value)

    def getMax(self):
        return self.minMaxStack[-1]['max']

    def getMin(self):
        return self.minMaxStack[-1]['min']


      


def main():
    stack = Stack()
    stack.push(9)
    stack.push(3)
    stack.push(9)
    stack.push(14)
    stack.push(2)
    print(stack.peek())
    print(stack.getMax())
    print(stack.getMin())
    print(stack.pop())
    print(stack.getMin())


if __name__ == "__main__":
    main()
