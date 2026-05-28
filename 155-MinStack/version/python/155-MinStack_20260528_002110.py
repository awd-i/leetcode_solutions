# Last updated: 5/28/2026, 12:21:10 AM
1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5
6    def push(self, val: int) -> None:
7        if not self.stack:
8            self.stack.append((val,val))
9            return
10        current_min = self.stack[-1][1]
11        self.stack.append((val, min(val, current_min)))
12
13    def pop(self) -> None:
14        self.stack.pop()
15        
16
17    def top(self) -> int:
18        return self.stack[-1][0]
19        
20
21    def getMin(self) -> int:
22        return self.stack[-1][1]
23        
24
25
26# Your MinStack object will be instantiated and called as such:
27# obj = MinStack()
28# obj.push(val)
29# obj.pop()
30# param_3 = obj.top()
31# param_4 = obj.getMin()