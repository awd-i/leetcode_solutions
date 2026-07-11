# Last updated: 7/11/2026, 3:20:08 PM
1class MovingAverage:
2
3    def __init__(self, size: int):
4        self.stream = deque()
5        self.sz = size
6        self.total = 0
7
8    def next(self, val: int) -> float:
9        self.stream.append(val)
10        self.total += val
11        if len(self.stream) > self.sz:
12            self.total -= self.stream.popleft()
13        return (self.total / len(self.stream))
14        
15
16
17# Your MovingAverage object will be instantiated and called as such:
18# obj = MovingAverage(size)
19# param_1 = obj.next(val)