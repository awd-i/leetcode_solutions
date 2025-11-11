# Last updated: 11/11/2025, 1:55:55 AM
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        answer = [0] * len(temperatures)
        for i, itemp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < itemp:
                previ = stack.pop()
                answer[previ] = i - previ
            stack.append(i)
        
        return answer




        
