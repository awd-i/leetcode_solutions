# Last updated: 11/11/2025, 1:58:07 AM
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
            
        def backtrack(curr, open, close):
            if open == 0 and close == 0:
                result.append(curr)
                return
        
            if open > 0:
                backtrack(curr + "(", open - 1, close)
            
            if close > open:
                backtrack(curr + ")", open, close - 1)

        backtrack("", n, n)
        return result


        