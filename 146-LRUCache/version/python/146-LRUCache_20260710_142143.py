# Last updated: 7/10/2026, 2:21:43 PM
1from collections import OrderedDict
2
3
4class LRUCache:
5    def __init__(self, capacity: int):
6        self.capacity = capacity
7        self.dict = OrderedDict()
8
9    def get(self, key: int) -> int:
10        if key not in self.dict:
11            return -1
12        self.dict.move_to_end(key, last=True)
13        return self.dict[key]
14
15    def put(self, key: int, value: int) -> None:
16        if key in self.dict:
17            self.dict[key] = value
18            self.dict.move_to_end(key, last=True)
19        else:
20            if len(self.dict) == self.capacity:
21                self.dict.popitem(last=False)
22            self.dict[key] = value
23
24
25# Your LRUCache object will be instantiated and called as such:
26# obj = LRUCache(capacity)
27# param_1 = obj.get(key)
28# obj.put(key,value)