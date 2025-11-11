// Last updated: 11/11/2025, 1:58:06 AM
class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack.contains(needle)) {
            return haystack.indexOf(needle);
        } else {
            return -1;
        }

    }
}