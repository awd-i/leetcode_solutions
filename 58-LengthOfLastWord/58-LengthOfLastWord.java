// Last updated: 11/11/2025, 1:57:55 AM
class Solution {
    public int lengthOfLastWord(String s) {
        String tempString = s.trim();
        int index = tempString.lastIndexOf(" ");
        if (index == 0) {
            return (s.length());
        }
        tempString = tempString.substring(index+1); //it counts the index as part of the substring
        return (tempString.length());
    }
} 