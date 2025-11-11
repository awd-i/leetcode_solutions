# Last updated: 11/11/2025, 1:57:40 AM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l, r = 0, 1
        mprofit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mprofit = max(mprofit, profit)
            else:
                l = r
            r += 1

        return mprofit
            

        