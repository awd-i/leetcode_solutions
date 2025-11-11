# Last updated: 11/11/2025, 1:55:29 AM
class Solution:
    def minOperations(self, n: int) -> int:
        result = 0
        while n > 0:
            if n % 2 == 0: # (n % 2 == 0) -> n >>= 1
                n >>= 1
            elif (n & 2) > 0: # (n & 2) > 0 -> n, result += 1
                n += 1
                result += 1
            else:
                result += 1 # else result += 1, n >>= 2
                n >>= 2
        return result # return result