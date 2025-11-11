# Last updated: 11/11/2025, 1:56:14 AM
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            result.append(value)
            p1 -= 1
            p2 -= 1

        if carry:
            result.append(carry)

        return "".join(str(x) for x in result[::-1])