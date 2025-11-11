// Last updated: 11/11/2025, 1:58:12 AM
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
      ListNode temp_node = new ListNode(0); // the head
      ListNode current_node = temp_node;
      while (list1 != null && list2 != null) {
        if (list1.val < list2.val) {
        current_node.next = list1;
        list1 = list1.next;
        } else {
        current_node.next = list2;
        list2 = list2.next;
      }
      current_node = current_node.next;
    }
    current_node.next = (list1 != null) ? list1 : list2;
    return temp_node.next;
}
}