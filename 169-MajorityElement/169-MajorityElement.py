# Last updated: 11/11/2025, 1:57:23 AM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)
                
      

        
