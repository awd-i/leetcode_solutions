# Last updated: 7/12/2026, 4:29:36 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4        ops = {"+", "*", "-", "/"}
5        for token in tokens:
6            if token in ops:
7                b = stack.pop() # last of stack
8                a = stack.pop() # one after last
9                if token == "+":
10                    stack.append(a+b)
11                if token == "-":
12                    stack.append(a-b)
13                if token == "/":
14                    stack.append(int(a / b))
15                if token == "*":
16                    stack.append(a * b)
17            else:
18                stack.append(int(token))
19        return stack.pop()