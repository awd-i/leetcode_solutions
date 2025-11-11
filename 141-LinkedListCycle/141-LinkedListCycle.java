// Last updated: 11/11/2025, 1:57:34 AM
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        Set<ListNode> lset = new HashSet<>();
        while (head != null) {
            if (lset.contains(head)) {
                return true;
            }
            lset.add(head);
            head = head.next;
        }
        return false;
    }
}