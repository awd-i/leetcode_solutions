# Last updated: 7/11/2026, 12:53:39 PM
1class TrieNode:
2    def __init__(self, char = ""):
3        self.char = ""
4        self.children = {}
5        self.is_end = False
6        
7class Trie:
8
9    def __init__(self):
10        self.root = TrieNode()
11
12    def insert(self, word: str) -> None:
13        node = self.root
14        for ch in word:
15            if ch in node.children:
16                node = node.children[ch]
17            else:
18                new_node = TrieNode(ch)
19                node.children[ch] = new_node
20                node = new_node
21        node.is_end = True
22
23    def search(self, word: str) -> bool:
24        node = self.root
25        for ch in word:
26            if ch not in node.children:
27                return False
28            node = node.children[ch]
29        return node.is_end
30
31    def startsWith(self, prefix: str) -> bool:
32        node = self.root
33        for ch in prefix:
34            if ch not in node.children:
35                return False
36            node = node.children[ch]
37        return True
38       
39
40
41# Your Trie object will be instantiated and called as such:
42# obj = Trie()
43# obj.insert(word)
44# param_2 = obj.search(word)
45# param_3 = obj.startsWith(prefix)