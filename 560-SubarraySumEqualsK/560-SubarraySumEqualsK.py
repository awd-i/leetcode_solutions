# Last updated: 11/11/2025, 1:56:05 AM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        S = 0
        prefix = {0: 1}  # prefix sum frequency

        for num in nums:
            S += num
            if S - k in prefix:
                count += prefix[S - k]
            prefix[S] = prefix.get(S, 0) + 1
        return count






        
                
