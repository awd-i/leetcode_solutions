# Last updated: 11/11/2025, 1:57:37 AM
from collections import Counter
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        freq = Counter(nums)
        k = 0
        maxl = 0
        for num in freq:
            if num - 1 not in freq:
                i = num
                k = 1
                while i + 1 in freq:
                    i += 1
                    k += 1
                maxl = max(maxl, k)
        return maxl

            

        
        