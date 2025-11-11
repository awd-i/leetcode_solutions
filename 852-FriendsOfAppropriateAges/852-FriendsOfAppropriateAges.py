# Last updated: 11/11/2025, 1:55:51 AM
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def dfs(age_x, age_y):
            return (age_y <= 0.5*age_x + 7) or (age_y > age_x) or (age_y > 100 and age_x < 100)
        dict1, total = Counter(ages), 0
        for k1, v1 in dict1.items():
            for k2, v2 in dict1.items():
                if not dfs(k1, k2):
                    total += v1 * v2
                    if k1 == k2:
                        total -= v1
        return total
                
                    
            
