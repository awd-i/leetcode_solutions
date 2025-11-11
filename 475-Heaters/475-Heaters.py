# Last updated: 11/11/2025, 1:56:09 AM
import collections
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort() # sort the houses and heaters for our algo to work
        heaters.sort()
        j = 0
        ans = 0

        for h in houses: # iterate through the houses
            while j + 1 < len(heaters) and abs(heaters[j + 1] - h) <= abs(heaters[j] - h):
                j += 1 # iterate until we find the closest heater, checks if the distance to the next heater is closer than the current heater
            ans = max(ans, abs(heaters[j]-h)) # max distance is the radius we'll need for the heaters to reach every house
        return ans
        
        

            

