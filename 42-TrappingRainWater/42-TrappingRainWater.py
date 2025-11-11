# Last updated: 11/11/2025, 1:57:58 AM
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxl = 0
        maxr = 0
        trapped = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < maxl:
                    trapped += maxl - height[l]
                else:
                    maxl = height[l]
                l += 1
            else: 
                if height[r] < maxr:
                    trapped += maxr - height[r]
                else:
                    maxr = height[r]
                r -= 1
        return trapped
                    

                

       
            
            
            



        