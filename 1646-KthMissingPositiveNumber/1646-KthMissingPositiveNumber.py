# Last updated: 11/11/2025, 1:55:34 AM
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr) - 1
        while l <= r:
            mid = (l+r) // 2
            if arr[mid] - mid - 1 < k: # arr[idx] - idx - 1 = missing positive numbers before the index 4 - 3 = 1
                l = mid + 1
            else:
                r = mid - 1
        return l + k # return the amount of digits missing + left, which is the arr[right] + k - (arr[right] - right - 1) = k + left 

