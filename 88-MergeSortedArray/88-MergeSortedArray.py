# Last updated: 11/11/2025, 1:57:46 AM
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        clone = nums1[:m]
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if clone[i] <= nums2[j]:
                nums1[k] = clone[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        if j == n:
            while i < m:
                nums1[k] = clone[i]
                k += 1
                i += 1
        if i == m:
            while j < n:
                nums1[k] = nums2[j]
                k += 1
                j += 1
        return 
        
        
        
        