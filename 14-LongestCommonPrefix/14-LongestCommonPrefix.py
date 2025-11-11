# Last updated: 11/11/2025, 1:58:14 AM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        prefix = strs[0] # make prefix the first word entirely
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0: # while prefix not in string, reduce it by reducing the length of prefix
                prefix = prefix[0 : len(prefix) - 1]
                if prefix == "":
                    return "" # if prefix becomes nothing, return nothing
        return prefix