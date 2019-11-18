class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
    
    def rightSideView(self, root):

        return False
        
    def rightSideViewMaster(self, root):
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val,
                level = [kid for node in level for kid in (node.left, node.right) if kid]
        return view
            

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


    print(fourTree.rightSideView(oneTree))
    print(fourTree.rightSideViewMaster(oneTree))
if __name__ == "__main__":
    main()
