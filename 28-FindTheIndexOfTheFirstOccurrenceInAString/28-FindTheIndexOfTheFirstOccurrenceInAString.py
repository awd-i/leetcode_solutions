# Last updated: 11/11/2025, 1:58:03 AM
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle not in haystack:
            return -1
        
        for i in range(len(haystack)-len(needle)+1):
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                    if j == len(needle) - 1:
                        return i
                    else:
                        j += 1
        
        return -1


        
        

        