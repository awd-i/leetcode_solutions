# Last updated: 11/11/2025, 1:57:28 AM
""" 
looking for a number where mid < l and mid < r
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
       
        if nums[r] > nums[0]:
            return nums[0]
        
        while r >= l:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1

            



