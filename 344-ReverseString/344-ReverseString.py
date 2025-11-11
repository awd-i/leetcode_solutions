# Last updated: 11/11/2025, 1:56:53 AM
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        return s
            
        