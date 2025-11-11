# Last updated: 11/11/2025, 1:55:42 AM
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        def is_subsequence(check, string):
            i = j = 0
            while i < len(check) and j < len(string):
                if check[i] == string[j]:
                    i += 1
                j += 1
            return i == len(check)
        
        source_chars = set(source)
        for char in target:
            if char not in source_chars:
                return -1
        
        concatenated_source = source
        count = 1
        while not is_subsequence(target, concatenated_source):
            concatenated_source += source
            count += 1
        return count