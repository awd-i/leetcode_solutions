# Last updated: 11/11/2025, 1:57:50 AM
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 2:
            return x
        
        r = x 
        while r > x // r:
            r = (r + x // r) // 2
        return r

        





        
        