# Last updated: 6/22/2026, 10:09:48 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stack = []
4        ops = {'+','*','-','/'}
5        for token in tokens:
6            if token in ops:
7                b = stack.pop()
8                a = stack.pop()
9                if token == '+': stack.append(a+b)
10                if token == '*': stack.append(a*b)
11                if token == '-': stack.append(a-b)
12                if token == '/': stack.append(int(a/b))
13            else:
14                stack.append(int(token))
15        return stack[0]