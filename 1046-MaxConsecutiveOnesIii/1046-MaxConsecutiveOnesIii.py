# Last updated: 11/11/2025, 1:55:42 AM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, maxLength, zeroes = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength
