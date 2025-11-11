# Last updated: 11/11/2025, 1:55:47 AM
class Solution:
    def fib(self, n: int) -> int:

        cache = {0: 0, 1: 1}

        def sequence(i):
            if i in cache:
                return cache[i]
            cache[i] = sequence(i-1) + sequence(i-2) # sums up previous numbers
            return cache[i]

        return sequence(n)
