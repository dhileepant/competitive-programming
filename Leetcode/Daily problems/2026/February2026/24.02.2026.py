# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, dna):
            if not node:
                return 0
            dna = dna * 2 + node.val
            if not node.left and not node.right:
                return dna
            return dfs(node.left, dna) + dfs(node.right, dna)
        
        return dfs(root, 0)
