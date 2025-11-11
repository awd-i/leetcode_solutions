# Last updated: 11/11/2025, 1:57:22 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = deque()
        q.append(root)
        q.append(None)
        rightsideview = []
        curr = root
        while q:
            prev, curr = curr, q.popleft()
            while curr:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                prev, curr = curr, q.popleft()
            rightsideview.append(prev.val)
            if q:
                q.append(None)

        return rightsideview
        
