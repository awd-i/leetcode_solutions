# Last updated: 11/11/2025, 1:57:42 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        tgt = []

        def navigator(node, lvl):
            if not node:
                return None
            if lvl == len(tgt):
                tgt.append([])
            tgt[lvl].append(node.val)
            navigator(node.left, lvl+1)
            navigator(node.right, lvl+1)
        
        navigator(root, 0)
        return tgt


        