# Last updated: 11/11/2025, 1:55:46 AM
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key = lambda p: p[0] ** 2 + p[1] ** 2) # everything sqrt so we can compare everything squared
        return points[:k]

