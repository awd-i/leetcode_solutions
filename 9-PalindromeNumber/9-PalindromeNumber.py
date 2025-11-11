# Last updated: 11/11/2025, 1:58:16 AM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
    
        string = str(x)
        return (string == string[::-1])
        