# Last updated: 11/11/2025, 1:57:18 AM
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '*' in node
            char = word[i]

            if char == '.':
                for child in node:
                    if child != '*' and dfs(node[child], i+1):
                        return True
                return False
            else:
                if char not in node:
                    return False
                return dfs(node[char], i+1)
            
        return dfs(self.root, 0)
            

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)