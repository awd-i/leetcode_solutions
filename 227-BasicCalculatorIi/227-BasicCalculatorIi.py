# Last updated: 11/11/2025, 1:57:13 AM
class Solution:
    def calculate(self, s: str) -> int:
        def update(op, v):
            if op == "+": stack.append(v)
            if op == "-": stack.append(-v)
            if op == "*": stack.append(stack.pop() * v)
            if op == "/": stack.append(int(stack.pop() / v))

        i = 0
        num = 0
        stack = []
        sign = "+"

        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i]) #add >10 digits up
            elif s[i] in "+-*/":
                update(sign, num)
                num, sign = 0, s[i]
            i += 1
            
        update(sign, num)
        return sum(stack)

        
    
        
