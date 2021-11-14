# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

lo = -1
hi = -1
treeVals = []
def traverse(node):
    if node is None:
        return
    if lo <= node.val <= hi:
        treeVals.append(node.val)
    if lo < node.val:
        traverse(node.left)
    if node.val < hi:
        traverse(node.right)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        global treeVals, lo, hi
        lo = low
        hi = high
        treeVals = []
        traverse(root)
        return sum(treeVals)
        
        

        