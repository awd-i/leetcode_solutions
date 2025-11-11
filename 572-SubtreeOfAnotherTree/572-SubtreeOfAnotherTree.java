// Last updated: 11/11/2025, 1:56:04 AM
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (isSameTree(root, subRoot)) {
            return true;
        }

        if (root == null) {
            return false;
        }
        
        if (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot)) {
            return true;
        }

        return false;
        
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        //  1.       1 
        // 2 3.     2. 3   //      //
        // 5. 6
        if (p == null && q == null ) {
            return true;
        }

        if (p == null || q == null) {
            return false;
        }

        if (p.val != q.val) {
            return false;
        }

        return ((isSameTree(p.right, q.right) && isSameTree(p.left, q.left)));
        
    }
}