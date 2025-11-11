# Last updated: 11/11/2025, 1:55:45 AM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        l = 0
        r = n - 1
        for i in range(n-1, -1, -1):
            if abs(nums[l]) < abs(nums[r]): # if the absolute value is more, then its squared value will be more
                square = nums[r]
                r -= 1
            else:
                square = nums[l]
                l += 1
            result[i] = square * square
        return result