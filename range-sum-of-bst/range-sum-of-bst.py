# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

treeVals = []
def traverse(node):
    if node is None:
        return
    treeVals.append(node.val)
    traverse(node.left)
    traverse(node.right)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        global treeVals
        treeVals = []
        traverse(root)
        inRange = [x for x in treeVals if low <= x <= high]
        return sum(inRange)
        
        

        