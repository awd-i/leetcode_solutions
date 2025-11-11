# Last updated: 11/11/2025, 1:55:40 AM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
                continue
            stack.append(c)
        return "".join(stack)
            