"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from
the root node down to the farthest leaf node.

Note:
    * This is just DFS returning the max(L, R) + 1 on the way back up.
    * LeetCode calls maxDepth(root) for you, so you don't have to create, call, and return the
      result from a helper function.

have to create

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1