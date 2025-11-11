# Last updated: 11/11/2025, 1:55:49 AM
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
    
        def hrs_needed(k):
            total = 0
            for p in piles:
                total += (p + k - 1) // k
            return total
        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if hrs_needed(m) <= h:
                r = m
            else:
                l = m + 1
        return l


            

        

        


        