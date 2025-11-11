# Last updated: 11/11/2025, 1:57:05 AM

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        heap = []
        intervals.sort(key = lambda x: x[0]) # sort by start time
        heapq.heappush(heap, intervals[0][1]) # push first and its end time
        for i in intervals[1:]: # check remaining
            if heap[0] <= i[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, i[1]) # queue another room with a new end time
        return len(heap)

        


        
        
            
            

        