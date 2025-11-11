# Last updated: 11/11/2025, 1:56:17 AM
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currNum = 0
        currStr = ''
        for c in s:
            if c == '[':
                stack.append(currStr)
                stack.append(currNum)
                currStr = ''
                currNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                currStr = prevString + num * currStr
            elif c.isdigit():
                currNum = 10 * currNum + int(c)
            else:
                currStr += c
        return currStr
                


