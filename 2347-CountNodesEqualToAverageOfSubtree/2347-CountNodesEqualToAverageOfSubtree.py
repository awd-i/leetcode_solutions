# Last updated: 11/11/2025, 1:55:30 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0
        def dfs(node):
            nonlocal result
            if node is None:
                return (0, 0)
            lsum, lcount = dfs(node.left)
            rsum, rcount = dfs(node.right)
            s = node.val + lsum + rsum
            c = 1 + lcount + rcount
            if s // c == node.val:
                result += 1
            return (s, c)
        dfs(root)
        return result
            

        