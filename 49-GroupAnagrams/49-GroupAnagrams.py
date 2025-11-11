# Last updated: 11/11/2025, 1:57:57 AM
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]

        return (list(d.values()))
        