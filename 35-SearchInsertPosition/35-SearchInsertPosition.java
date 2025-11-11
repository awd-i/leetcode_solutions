// Last updated: 11/11/2025, 1:58:00 AM
class Solution {
    public int searchInsert(int[] nums, int target) {
        for (int i = 0; i<nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
            else if (nums[i]>target) {
                return i;
            }
        }
        return (nums.length);
    }
}