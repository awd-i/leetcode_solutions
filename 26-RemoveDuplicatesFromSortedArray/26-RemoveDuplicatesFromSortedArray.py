# Last updated: 11/11/2025, 1:58:04 AM
class Solution(object):
    def removeDuplicates(self, nums):
        """
        two ways of approaching, make a set then just return convert the set to array or use two pointer(?)
        """
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return 0
        
        i = 0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i = i+1
                nums[i] = nums[j]
        
        return i+1







        





        