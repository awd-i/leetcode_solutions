# Last updated: 11/11/2025, 1:55:28 AM
class Solution(object):
    def hasSameDigits(self, s):
        if len(s) == 2:
            return s[0] == s[1]  
        
        tgt = ""  
        
        for i in range(len(s) - 1):  
            tgt += str((int(s[i]) + int(s[i+1])) % 10)  
        
        return self.hasSameDigits(tgt)