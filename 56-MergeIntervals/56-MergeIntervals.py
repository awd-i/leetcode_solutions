# Last updated: 11/11/2025, 1:57:54 AM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0]) # sort by first digit
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]: # check if the end point of the last in merged is less than the start of interval[0]. Basically if the start time is after, we have a new interval
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1]) # else find the max of the last interval in merged's end and intervals end.
        return merged
       



        

        

        



