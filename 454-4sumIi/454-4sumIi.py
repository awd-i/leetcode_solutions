# Last updated: 11/11/2025, 1:56:10 AM
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        cnt = 0
        m = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                m[a+b] += 1
        for c in nums3:
            for d in nums4:
                cnt += m[-(c+d)] #c+d must equal a+b negatively, so if we check the negative of c+d, then if the pairs in the hashmap, they will equal 0 together
        return cnt
        
