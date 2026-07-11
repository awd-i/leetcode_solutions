# Last updated: 7/11/2026, 2:27:18 PM
1import random
2class RandomizedSet:
3
4    def __init__(self):
5        self.d = {}
6        self.l = []
7        
8
9    def insert(self, val: int) -> bool:
10        if val in self.d:
11            return False
12        self.d[val] = len(self.l) # store index
13        self.l.append(val) # dont have to worry about displacement yet cuz not added
14        return True
15        
16    def remove(self, val: int) -> bool:
17        if val not in self.d:
18            return False
19        last_val, index = self.l[-1], self.d[val]
20        self.d[last_val] = index
21        self.l[-1] = self.l[index]
22        self.l[index] = last_val
23        self.l.pop()
24        del self.d[val]
25        return True
26
27    def getRandom(self) -> int:
28        return (random.choice(self.l))
29
30
31# Your RandomizedSet object will be instantiated and called as such:
32# obj = RandomizedSet()
33# param_1 = obj.insert(val)
34# param_2 = obj.remove(val)
35# param_3 = obj.getRandom()