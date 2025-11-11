# Last updated: 11/11/2025, 1:57:16 AM
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in nums:
            heapq.heappush(heap, -i)
        j = k 
        num = 0
        while j:
            num = heapq.heappop(heap)
            j -= 1
        return -num


        