# Last updated: 11/11/2025, 1:56:03 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def trees(t1, t2):
            if t1 is None:
                return t2
            if t2 is None:
                return t1
            t1.val += t2.val
            t1.left = trees(t1.left, t2.left)
            t1.right = trees(t1.right, t2.right)
            return t1

        return trees(root1, root2)
        


                
    
        
        