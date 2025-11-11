# Last updated: 11/11/2025, 1:56:57 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        table = defaultdict(list)
        q = deque([(root, 0)])     
        while q:
            node, col = q.popleft()
            if node is not None:
                table[col].append(node.val)
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))

        return [table[x] for x in sorted(table.keys())]




                
    

