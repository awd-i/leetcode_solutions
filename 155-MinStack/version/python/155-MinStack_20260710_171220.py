# Last updated: 7/10/2026, 5:12:20 PM
1class MedianFinder:
2
3    def __init__(self):
4        self.maxHeap = [] # heapq for top of lower half
5        self.minHeap = [] # heapq for bottom of upper half
6
7    def addNum(self, num: int) -> None: # we wanna stick numbers in order
8        heappush(self.maxHeap, -num) # top of lower half
9        heappush(self.minHeap, -heappop(self.maxHeap)) # push the top of the lower half heap into the upper half
10        if (len(self.maxHeap) < len(self.minHeap)): # we want to store the middle element in lower half
11            heappush(self.maxHeap, -heappop(self.minHeap)) # push middle to maxHeap[0]
12
13    def findMedian(self) -> float:
14        if (len(self.minHeap) < len(self.maxHeap)): # odd number
15            return -self.maxHeap[0] # largest part of bottom half
16        return (-self.maxHeap[0] + self.minHeap[0]) / 2
17
18        
19
20
21# Your MedianFinder object will be instantiated and called as such:
22# obj = MedianFinder()
23# obj.addNum(num)
24# param_2 = obj.findMedian()