# Last updated: 11/11/2025, 1:57:38 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        maxSum = float('-inf')
        def dfs(node):
            nonlocal maxSum
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            candidate = node.val + left + right
            maxSum = max(candidate, maxSum)
            return node.val + max(left, right)
        dfs(root)
        return maxSum


            