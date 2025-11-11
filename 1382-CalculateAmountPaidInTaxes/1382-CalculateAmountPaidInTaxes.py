# Last updated: 11/11/2025, 1:55:35 AM
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = 0
        prev = 0
        for upper, p in brackets:
            if income >= upper:
                tax += (upper-prev) * p / 100
                prev = upper
            else: 
                tax += (income - prev) * p / 100
                return tax
        
        return tax