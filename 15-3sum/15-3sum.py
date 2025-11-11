# Last updated: 11/11/2025, 1:58:13 AM
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []

        target = 0
        nums.sort()
        n = len(nums)
        nummies = []

        for f in range(n):
            if f > 0 and nums[f] == nums[f-1]:
                continue
            s, t = f + 1, n - 1
            while s < t:
                total = nums[f] + nums[s] + nums[t]
                if total == target:
                    nummies.append([nums[f],nums[s],nums[t]])
                    while s < t and nums[s] == nums[s+1]:
                        s+=1
                    while s > t and nums[t] == nums[t-1]:
                        t-= 1
                    
                    s += 1
                    t -= 1
                elif total < target:
                    s += 1
                else:
                    t -= 1

        return list(nummies)
        

            

            