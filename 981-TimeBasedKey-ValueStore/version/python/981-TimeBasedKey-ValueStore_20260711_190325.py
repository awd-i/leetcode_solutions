# Last updated: 7/11/2026, 7:03:25 PM
1import collections
2class TimeMap:
3
4    # timestamps[timestamp] = dict, index
5
6    def __init__(self):
7        self.store = {} # key = timestamp, value
8
9    def set(self, key: str, value: str, timestamp: int) -> None:
10        if key not in self.store:
11            self.store[key] = []
12        self.store[key].append((timestamp, value))
13
14    def get(self, key: str, timestamp: int) -> str:
15        if key not in self.store:
16            return ""
17        if timestamp < self.store[key][0][0]:
18            return ""
19        l = 0
20        r = len(self.store[key])
21        while l < r:
22            mid = (l + r) // 2
23            if self.store[key][mid][0] > timestamp:
24                r = mid
25            else:
26                l = mid + 1
27        return "" if r == 0 else self.store[key][r - 1][1]
28        