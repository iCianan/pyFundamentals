# Write a function that takes in Binary Tree and inverts it. In other words
# the function should swap every left node in the tree for its corresponding right node.
# Each binary tree node has a value stored in a property called "value" and two children
# nodes stored in properties called "left" and "right" respectively. Children nodes
# can either be Binary Tree nodes themselves or the None value.

# Sample Input:
#           1
#        /    \
#       2      3
#     /   \   /  \
#    4     5 6    7
#   / \  
#  8   9

#  Sample Output:

#           1
#        /    \
#       3      2
#     /   \   /  \
#    7     6 5    4
#                / \  
#               9   8
from collections import deque
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
    
    def invertBinaryTree(self, root):
        queue = deque([root])
        while len(queue):
            current = queue.popleft()
            if current is None:
                continue
            self.swapLeftAndRight(current)
            queue.append(current.left)
            queue.append(current.right)

    def invertBinaryTreeRecursive(self, root):
        if root is None:
            return
        self.swapLeftAndRight(root)
        self.invertBinaryTreeRecursive(root.left)
        self.invertBinaryTreeRecursive(root.right)

    def swapLeftAndRight(self, tree):
        tree.left, tree.right = tree.right, tree.left        

def main():
    oneTree   = TreeNode(1)
    twoTree   = TreeNode(2)
    threeTree = TreeNode(3)
    fourTree  = TreeNode(4)
    fiveTree  = TreeNode(5)
    sixTree  = TreeNode(6)
    sevenTree  = TreeNode(7)    
    eightTree  = TreeNode(8)
    nineTree  = TreeNode(9)
    oneTree.left = twoTree
    oneTree.right = threeTree
    twoTree.left = fourTree
    twoTree.right = fiveTree
    threeTree.left = sixTree
    threeTree.right = sevenTree    
    fourTree.left = eightTree
    fourTree.right = nineTree   

    print(oneTree.invertBinaryTree(oneTree))    
if __name__ == "__main__":
    main()
