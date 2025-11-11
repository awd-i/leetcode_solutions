# Last updated: 11/11/2025, 1:55:38 AM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1 # either adds what was in x or 0 for the value + 1. same as if freq[x] add 1 else set freq[x] to 0

        return len(freq) == len(set(freq.values()))
