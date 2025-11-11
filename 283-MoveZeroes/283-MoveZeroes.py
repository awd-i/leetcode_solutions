# Last updated: 11/11/2025, 1:57:00 AM
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k] = nums[i]
                k += 1
        for j in range(k, len(nums)):
            nums[j] = 0

                
                
            
                        
                       
            
        