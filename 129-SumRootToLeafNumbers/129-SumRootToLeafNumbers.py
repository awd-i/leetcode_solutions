# Last updated: 11/11/2025, 1:57:36 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node, string):
            if not node:
                return 0
            string += str(node.val)
            if not node.left and not node.right:
                return int(string)
            return dfs(node.left, string) + dfs(node.right, string)
        total = dfs(root, "")
        return total

