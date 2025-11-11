# Last updated: 11/11/2025, 1:56:16 AM
import random
class Solution:

    def __init__(self, nums: List[int]):
        self.book = defaultdict(list)
        for i, num in enumerate(nums):
            self.book[num].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.book[target])
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)