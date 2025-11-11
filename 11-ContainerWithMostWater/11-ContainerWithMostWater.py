# Last updated: 11/11/2025, 1:58:15 AM
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mxa = 0
        area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = h * w
            mxa = max(mxa, area)

            if height[l] < height[r]:
                l += 1
            else: 
                r -= 1

        return mxa
                
       

        

        

        




        