# Last updated: 11/11/2025, 1:55:59 AM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == None:
            return True
        if len(s) == 1:
            return True
        def isPalindrome(str, i, j):
            while i < j:
                if s[i] != s[j]: # middle value doesnt matter
                    return False
                i += 1
                j -= 1
            return True
        i = 0
        j = len(s) - 1
        
        while i < j:
            if s[i] != s[j]:
                return (isPalindrome(s, i, j-1) or isPalindrome(s, i+1, j))
            i += 1
            j -= 1
        return True
            