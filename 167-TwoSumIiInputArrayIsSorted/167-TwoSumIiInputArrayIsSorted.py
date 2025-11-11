# Last updated: 11/11/2025, 1:57:25 AM
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

    
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1, r+1]
            elif total < target:
                l += 1
            elif total > target:
                r -= 1
        

                


        