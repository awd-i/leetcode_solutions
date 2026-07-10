# Last updated: 7/10/2026, 3:40:37 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minElem = []
6
7    def push(self, value: int) -> None:
8        if (self.minElem == []) or (value <= self.minElem[-1]):
9            self.minElem.append(value)
10        self.stack.append(value)
11
12    def pop(self) -> None:
13        elem = self.stack.pop()
14        if self.minElem[-1] == elem:
15            self.minElem.pop()
16
17
18    def top(self) -> int:
19        if self.stack:
20            return self.stack[-1]
21        else:
22            return -1
23
24    def getMin(self) -> int:
25        if self.minElem:
26            return self.minElem[-1]
27        else:
28            return -1
29
30
31# Your MinStack object will be instantiated and called as such:
32# obj = MinStack()
33# obj.push(value)
34# obj.pop()
35# param_3 = obj.top()
36# param_4 = obj.getMin()
37
38