# Last updated: 11/11/2025, 1:55:33 AM
class SparseVector:
    def __init__(self, nums: List[int]):
        self.book = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.book[i] = nums[i]
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        for i, n in self.book.items():
            if i in vec.book:
                result += n * vec.book[i]
        return result
        
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)