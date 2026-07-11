# Last updated: 7/11/2026, 4:49:10 PM
1class MyCircularQueue:
2
3    def __init__(self, k: int):
4        self.queue = [0] * k # queue to store items
5        self.capacity = k # capacity to store numbers
6        self.count = 0 # how many items in circular queue
7        self.head = 0 # index of the first item
8
9
10    def enQueue(self, value: int) -> bool:
11        if (self.count == self.capacity):
12            return False # full queue
13        self.queue[(self.head + self.count) % self.capacity] = value # dont have to subtract bc we dont update count
14        self.count += 1
15        return True
16
17    def deQueue(self) -> bool:
18        if (self.count == 0):
19            return False # empty queue
20        self.head = (self.head + 1) % self.capacity # shift head up since head = last
21        self.count -= 1
22        return True
23        
24    def Front(self) -> int:
25        if self.count != 0:
26            return self.queue[self.head]
27        return -1
28        
29
30    def Rear(self) -> int:
31        if self.count != 0:
32            return self.queue[(self.head + self.count - 1) % self.capacity]
33        return -1
34        
35    def isEmpty(self) -> bool:
36        return (self.count == 0)
37
38    def isFull(self) -> bool:
39        return (self.count == self.capacity)
40        
41
42
43# Your MyCircularQueue object will be instantiated and called as such:
44# obj = MyCircularQueue(k)
45# param_1 = obj.enQueue(value)
46# param_2 = obj.deQueue()
47# param_3 = obj.Front()
48# param_4 = obj.Rear()
49# param_5 = obj.isEmpty()
50# param_6 = obj.isFull()