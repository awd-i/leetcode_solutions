# Last updated: 7/11/2026, 7:05:40 PM
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        l = 0
4        r = len(nums) - 1
5        while l < r:
6            mid = (l + r) // 2
7            if nums[mid] > nums[mid+1]:
8                r = mid
9            else:
10                l = mid + 1
11        return l
12            