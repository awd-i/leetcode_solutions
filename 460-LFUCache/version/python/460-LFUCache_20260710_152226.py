# Last updated: 7/10/2026, 3:22:26 PM
1import collections
2
3class LFUCache:
4
5    def __init__(self, capacity: int):
6        self.cache = {}
7        self.frequencies = defaultdict(OrderedDict)
8        self.minf = 0
9        self.capacity = capacity
10
11    def insert(self, key, freq, value):
12        self.cache[key] = (freq, value)
13        self.frequencies[freq][key] = value
14
15    def get(self, key: int) -> int:
16        if key not in self.cache:
17            return -1
18        freq, val = self.cache[key]
19        del self.frequencies[freq][key]
20        if not self.frequencies[freq]:
21            del self.frequencies[freq]
22            if freq == self.minf:
23                self.minf += 1
24        self.insert(key, freq + 1, val)
25        return val
26
27    def put(self, key: int, value: int) -> None:
28        if key in self.cache:
29            freq = self.cache[key][0]
30            self.cache[key] = (freq, value) # only accessed, so freq doesnt change
31            self.get(key)
32            return
33        if self.capacity == len(self.cache):
34            key_to_delete, _ = self.frequencies[self.minf].popitem(last=False)
35            del self.cache[key_to_delete]
36        self.minf = 1
37        self.insert(key, 1, value)
38        return
39            
40
41# Your LFUCache object will be instantiated and called as such:
42# obj = LFUCache(capacity)
43# param_1 = obj.get(key)
44# obj.put(key,value)