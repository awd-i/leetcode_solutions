# Last updated: 11/11/2025, 1:57:55 AM
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 1:
            return 1 / self.myPow(x, -n)
        div = self.myPow(x, n//2)
        if n % 2 == 0:
            return div * div
        else:
            return x * div * div
            
           
        
            

            
        
