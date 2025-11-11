# Last updated: 11/11/2025, 1:55:31 AM
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        oceanView = []
        r = len(heights) - 1
        globalMax = float('-inf')
        while r > -1:
            if r == len(heights) - 1:
                oceanView.append(r)
                globalMax = heights[r]
                r -= 1
                continue
            else:
                if heights[r] > globalMax:
                    globalMax = heights[r]
                    oceanView.append(r)
                r -= 1
        return oceanView[::-1]
      
            




