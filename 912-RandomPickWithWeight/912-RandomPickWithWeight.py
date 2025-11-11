# Last updated: 11/11/2025, 1:55:48 AM
import math
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum
        
    def pickIndex(self) -> int:
        tgt = self.total_sum * random.random()
        for i, prefix_sum in enumerate(self.prefix_sums):
            if tgt < prefix_sum:
                return i
        


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()