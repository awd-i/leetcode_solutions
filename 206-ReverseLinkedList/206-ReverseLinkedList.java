// Last updated: 11/11/2025, 1:57:28 AM
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        
        ListNode prev = null;
        ListNode curr = head;
        while (curr != null) {
            ListNode old_next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = old_next;
        }
        return prev;
    }
}