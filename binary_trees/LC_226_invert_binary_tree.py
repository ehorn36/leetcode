"""
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.
(switch places of all child nodes)

Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

Example 3:
    Input: root = []
    Output: []
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        # Base case (not a valid node)
        if root is None:
            return None

        # Traverse left and right children nodes (DFS)
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Swap left / right child nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        return root

node1 = TreeNode()
node1.val = 1
node1.left = None
node1.right = None

node3 = TreeNode()
node3.val = 3
node3.left = None
node3.right = None

node2 = TreeNode()
node2.val = 2
node2.left = node1
node2.right = node3

node6 = TreeNode()
node6.val = 6
node6.left = None
node6.right = None

node9 = TreeNode()
node9.val = 9
node9.left = None
node9.right = None

node7 = TreeNode()
node7.val = 7
node7.left = node6
node7.right = node9

node4 = TreeNode()
node4.val = 4
node4.left = node2
node4.right = node7

node0 = TreeNode()
node0.val = 0
node0.left = None
node0.right = None


test = Solution()
print(test.invertTree(node4).val)
