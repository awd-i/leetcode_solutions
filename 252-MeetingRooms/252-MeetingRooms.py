# Last updated: 11/11/2025, 1:57:06 AM
class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        results = []
        i = 0
        j = 1
        n = len(intervals)

        if len(intervals) == 1 or intervals is None:
            return True

        while j < n:
            if intervals[i][0] == intervals[j][0]:
                return False
            if intervals[j][0] < intervals[i][1] <= intervals[j][1]:
                return False
            if intervals[j][1] <= intervals[i][1]:
                return False
            i += 1
            j += 1
        return True



        
