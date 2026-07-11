# Last updated: 7/11/2026, 4:06:32 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        def dfs(node, string):
17            if node is None:
18                string += "None,"
19            else:
20                string += str(node.val) + ","
21                string = dfs(node.left, string)
22                string = dfs(node.right, string)
23            return string
24        
25        return dfs(root, "")
26        
27
28    def deserialize(self, data):
29        """Decodes your encoded data to tree.
30        
31        :type data: str
32        :rtype: TreeNode
33        """
34
35        def bfs(l):
36            if l[0] == 'None': # base case
37                l.pop(0)
38                return None
39
40            root = TreeNode(l[0])
41            l.pop(0)
42            root.left = bfs(l)
43            root.right = bfs(l)
44            return root
45
46        lst = data.split(",")
47        root = bfs(lst)
48        return root
49        
50
51# Your Codec object will be instantiated and called as such:
52# ser = Codec()
53# deser = Codec()
54# ans = deser.deserialize(ser.serialize(root))