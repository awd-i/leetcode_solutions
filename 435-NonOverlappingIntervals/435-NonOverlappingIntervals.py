# Last updated: 11/11/2025, 1:56:13 AM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        if intervals is None or len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda x: x[0])
        i = 0
        count = 0
        for j in range(1, len(intervals)):
            if intervals[j][0] < intervals[i][1]: #delete j by default and compares next one after j
                count += 1
                if intervals[j][1] < intervals[i][1]: #delete i and compares j and the next one after j
                    i = j
            else:
                i = j
        return count
