"""
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root. The length of a path between two nodes is
represented by the number of edges between them.

Note - Diameter != height.

    * If root's L.height = 0 and R.height = 3, root.height = max(0, 3) = 3

    * If we calculate diameter as L + R, then root.diameter = 3

    * However, R.L.height = 2, R.R.height = 2, R.diameter = (2 + 2) = 4
    
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        diameter = [0]

        # Finds the height of a node
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Diameter = left height + right height
            diameter[0] = max(diameter[0], left + right)

            # Return height
            return max(left, right) + 1

