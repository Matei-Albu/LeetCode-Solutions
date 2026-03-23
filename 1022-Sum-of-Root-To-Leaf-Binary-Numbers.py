# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int
        def sum_root(node, current ):
            if not node:
                return 0
            
            current = current * 2 + node.val

            if not node.left and not node.right:
                return current

            return sum_root(node.left, current) + sum_root(node.right,current)
        return sum_root(root,0)

