# Last updated: 11/11/2025, 1:57:51 AM
class Solution(object):
    def plusOne(self, digits):

        i = len(digits) - 1

        while (i > -1):
            if digits[i] == 9 and i == 0:
                digits[i] = 0
                digits = [1] + digits
                i = -1
            elif digits[i] < 9:
                digits[i] += 1
                i = -1
            else:
                digits[i] = 0
                i -= 1
                
            

        return digits
        
        