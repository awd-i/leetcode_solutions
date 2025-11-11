# Last updated: 11/11/2025, 1:58:11 AM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'}':'{',']':'[',')':'('}
        for char in s:
            if char in brackets:
                if stack == []:
                    return False
                if stack.pop() != brackets[char]:
                    return False
            else:
                stack.append(char)

        return not stack
