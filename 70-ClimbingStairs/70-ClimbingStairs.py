# Last updated: 11/11/2025, 1:57:50 AM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1): # if its 2 it just doesn't loop at all
            third = first + second 
            first = second
            second = third
        return second
        