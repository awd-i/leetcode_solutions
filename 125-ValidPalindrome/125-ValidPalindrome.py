# Last updated: 11/11/2025, 1:57:39 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tgt = ""
        for c in s:
            if c.isalnum():
                tgt += c.lower()
        
        i = 0
        j = len(tgt) - 1
        while i < j:
            if tgt[i] != tgt[j]:
                return False
            i += 1
            j -= 1
        return True
