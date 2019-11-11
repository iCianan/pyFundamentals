# Importing the library
from collections import deque


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return self
        else:
            current = self.root
            while(current):
                if value < current.value:
                    if current.left == None:
                        current.left = newNode
                        return self
                    else:
                        current = current.left
                else:
                    if current.right == None:
                        current.right = newNode
                        return self
                    else:
                        current = current.right

    def contains(self, value):
        current = self.root
        while(current):
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True
        return False

    def remove(self, value):
        return self

    def inOrderDFS(self, node):
        if node != None:
            self.inOrderDFS(node.left)
            print(node.value)
            self.inOrderDFS(node.right)

    def preOrderDFS(self, node):
        if node != None:
            print(node.value)
            self.preOrderDFS(node.left)
            self.preOrderDFS(node.right)

    def postOrderDFS(self, node):
        if node != None:
            self.postOrderDFS(node.left)
            self.postOrderDFS(node.right)
            print(node.value)

    def BFS(self):
        visited = []
        willVisit = deque()
        current = self.root
        willVisit.append(current)
        while(len(willVisit) > 0):
            current = willVisit.popleft()
            visited.append(current.value)
            if current.left:
                willVisit.append(current.left)
            if current.right:
                willVisit.append(current.right)
        return visited

    def validateBst(self, tree):
        return self.bstHelper(tree, float("-inf"), float("inf"))

    def bstHelper(self, tree, min, max):
        if tree is None:
            return True
        if tree.value < min or tree.value >= max:
            return False
        leftChild = self.bstHelper(tree.left, min, tree.value)
        return leftChild and self.bstHelper(tree.right, tree.value, max)
    
    def isValidBST(self, root) -> bool:     
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            current = queue.popleft()
            if current.left != None:
                if current.value <= current.left.value:
                    return False
                queue.append(current.left)
            if current.right != None:
                if current.value >= current.right.value:
                    return False
                queue.append(current.right)
        return True        
        


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def main():
    bst = BST()
    bst.insert(10)
    bst.insert(25)
    bst.insert(12)
    bst.insert(7)
    bst.insert(9)
    print(bst.validateBst(bst.root))
    print(bst.isValidBST(bst.root))



if __name__ == "__main__":
    main()
