# Last updated: 11/11/2025, 1:57:06 AM
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotatedDigits = {'0' : '0', '1' : '1', '8' : '8', '6' : '9', '9' : '6'}
        reverseString = []
        for c in reversed(num):
            if c not in rotatedDigits:
                return False
            reverseString.append(rotatedDigits[c])
        rotated = "".join(reverseString)
        return rotated == num
