# Last updated: 11/13/2025, 12:55:49 PM
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        if children is None:
            children = []
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        def do(node):
            if not node:
                return ['#']
            ans = [str(node.val)]
            for r in node.children:
                ans += do(r)
            ans.append("#")  
            return ans
        return ' '.join(do(root))
        
	
    def deserialize(self, data: str) -> 'Node':
        def dfs():
            val = next(data)
            if val != '#':
                node = Node(int(val), [])
                child = dfs()
                while child:
                    node.children.append(child)
                    child = dfs()
                return node
        data = iter(data.split())
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))