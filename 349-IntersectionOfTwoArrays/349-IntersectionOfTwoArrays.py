# Last updated: 11/11/2025, 1:56:53 AM
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        snums1 = set(nums1)
        snums2 = set(nums2)
        inter = list(snums1.intersection(snums2))
        return (inter)
        
       

        
        
        