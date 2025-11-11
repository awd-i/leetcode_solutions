# Last updated: 11/11/2025, 1:57:33 AM
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = 0
        for i in nums:
            unique ^= i
        return unique
        
        
        