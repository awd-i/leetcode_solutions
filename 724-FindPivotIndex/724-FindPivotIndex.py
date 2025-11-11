# Last updated: 11/11/2025, 1:55:56 AM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == (totalSum - leftSum - nums[i]): #Totalsum is the right sum, as you progress the leftSum gets bigger, remove the integer from the totalSum, as you progress remove it from the leftSum
                return i
            leftSum += nums[i]
        return -1


