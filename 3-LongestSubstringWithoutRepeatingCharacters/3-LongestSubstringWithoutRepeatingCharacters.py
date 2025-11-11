# Last updated: 11/11/2025, 1:58:16 AM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        seen = set()
        maxSeen = 0
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxSeen = max(maxSeen, r - l + 1)
        
        return maxSeen
            
                



                
        


