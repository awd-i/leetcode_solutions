# Last updated: 11/11/2025, 1:56:08 AM
class Solution:
    import functools
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = sum(nums)
        if target > s or target < -s:
            return 0
        @lru_cache(None)
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            plus = dfs(i + 1, total + nums[i])
            minus = dfs(i + 1, total - nums[i])
            return (plus + minus)

        return dfs(0, 0)