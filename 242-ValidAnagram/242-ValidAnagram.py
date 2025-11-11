# Last updated: 11/11/2025, 1:57:09 AM
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = Counter(s)
        chars2 = Counter(t)
        return chars == chars2