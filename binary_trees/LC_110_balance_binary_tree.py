"""
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: true

    Example 2:
        Input: root = [1,2,2,3,3,null,null,4,4]
        Output: false

    Example 3:
        Input: root = []
        Output: true

    Approach:
        * If node is null, return 0
        * Recursively find the height of the left subtree and right subtree
        * Add height on way up, so max(left, right) + 1
        * Return true if balanced, otherwise false
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        # Global variable to track if height is balanced
        balanced = [True]

        # Helper function
        def height(root):

            # If balanced[0] is False, all future calls are stopped
            if not root or balanced[0] is False:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            # Since we don't know which side will be bigger, use abs()
            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

            # Height is calculated on the way up, so add +1 when returning.
            return max(left_height, right_height) + 1

        # Call helper function
        height(root)

        # Return T or F
        return balanced[0]



node_10 = TreeNode(10)  # root
node_8 = TreeNode(8)
node_11 = TreeNode(11)
node_6 = TreeNode(6)
node_9 = TreeNode(9)
node_5 = TreeNode(5)
node_7 = TreeNode(7)

node_10.left = node_8
node_10.right = node_11
node_8.left = node_6
node_8.right = node_9
node_6.left = node_5
node_6.right = node_7

test = Solution()
print(test.isBalanced(node_10))