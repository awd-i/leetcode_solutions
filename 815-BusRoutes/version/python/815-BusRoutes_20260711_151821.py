# Last updated: 7/11/2026, 3:18:21 PM
1class MovingAverage:
2
3    def __init__(self, size: int):
4        self.stream = deque()
5        self.sz = size
6
7    def next(self, val: int) -> float:
8        self.stream.append(val)
9        if len(self.stream) > self.sz:
10            self.stream.popleft()
11        if len(self.stream) == 0:
12            return 0
13        return (sum(self.stream) / len(self.stream))
14        
15
16
17# Your MovingAverage object will be instantiated and called as such:
18# obj = MovingAverage(size)
19# param_1 = obj.next(val)