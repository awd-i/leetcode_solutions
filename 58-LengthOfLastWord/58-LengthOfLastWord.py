# Last updated: 11/11/2025, 1:57:53 AM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        Count last word
        """ 

        length = 0
        i = len(s) - 1

        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
        
                

                
                
        return len(seen)


        