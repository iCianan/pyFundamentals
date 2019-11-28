class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        self.insertBefore(self.head, newNode)
        
    def setTail(self, value):
        newNode = Node(value)
        if self.tail == None:
            self.head = newNode
            self.tail = newNode
        self.insertAfter(self.tail, newNode)

    def insertBefore(self, node, nodeToInsert):
        temp = node.prev
        nodeToInsert.next = node
        nodeToInsert.prev = temp
        if temp == None:
            self.head = nodeToInsert
        temp.next = nodeToInsert
        node.prev = nodeToInsert
        
    def insertAfter(self, node, nodeToInsert):
        temp = node.next
        nodeToInsert.next = temp
        nodeToInsert.prev = node
        if temp == None:
            self.tail = nodeToInsert
        temp.prev = nodeToInsert
        node.next = nodeToInsert

    def remove(self, node):
        pass


def main():
    list = DoublyLinkedList()
    list.setHead()    