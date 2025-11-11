# Last updated: 11/11/2025, 1:55:36 AM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        lc = 0
        rc = 0
        stack = []

        # pass 1
        for char in s:
            if char == '(':
                lc += 1
            elif char == ')':
                rc += 1
            if rc > lc:
                rc -= 1
            else:
                stack.append(char)
        
        # pass 2
        result = ""
        while stack:
            char = stack.pop()
            if lc > rc and char == "(":
                lc -= 1
            else:
                result += char
        
        return result[::-1]