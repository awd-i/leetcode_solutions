// Last updated: 11/11/2025, 1:58:18 AM
class Solution {
    public boolean isPalindrome(int x) {
        String str = Integer.toString(x);
        String tempStr = "";
        for (int j = (str.length()-1); j>=0; j--) {
            tempStr = tempStr + str.charAt(j);
        }
        return (tempStr.equals(str));
    }
}