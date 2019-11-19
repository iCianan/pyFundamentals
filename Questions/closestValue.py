from collections import deque
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
    
    def closestValue(self, root, target, closest = float('inf')): 
        if root is None:
            return       
        if abs(root.val - target) < abs(closest - target):
            closest = root.val
        if target < root.val:
            self.closestValue(root.left, target, closest)
        if target > root.val:
            self.closestValue(root.right, target, closest)
        return closest

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
    
    oneTree.right = twoTree


    # fourTree.left = twoTree
    # fourTree.right = fiveTree

    # twoTree.left = oneTree
    # twoTree.right = threeTree   


    print(oneTree.closestValue(oneTree, 3.428571))    
if __name__ == "__main__":
    main()



