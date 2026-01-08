"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

Example 1:
    Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
    Output: 6
    Explanation: The LCA of nodes 2 and 8 is 6.

Notes:
    * The root node is an ancestor for every other node in the BST.
    * The LCA is the lowest node in the tree that's an ancestor to nodes P and Q
    * Per the problem definition, the LCA can also be P or Q and must exist

To solve this problem, look at each node starting at the lowest known ancestor, AKA the root. If P and Q are both
smaller than the root, then look at the left node / subtree. If they're both bigger than the root, look at the
right subtree. If the root is in the middle of P and Q, or IS P or Q, then you've found the LCA.

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Recursive function that searches a left or right subtree until the supplied root value is between the values
        of P and Q, or equals P or Q. Returns a node object.
        """

        # If root value > both P & Q, search left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If root value < both P & Q, search right subtree
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Return the current root, which is between values of P and Q, or is P or Q.
        return root


# Create nodes
node_6 = TreeNode(6)
node_2 = TreeNode(2)
node_8 = TreeNode(8)
node_0 = TreeNode(0)
node_4 = TreeNode(4)
node_7 = TreeNode(7)
node_9 = TreeNode(9)
node_3 = TreeNode(3)
node_5 = TreeNode(5)

# Create tree
node_6.left = node_2
node_6.right = node_8
node_2.left = node_0
node_2.right = node_4
node_8.left = node_7
node_8.right = node_9
node_4.left = node_3
node_4.right = node_5

# Tests
# root, p, q = node_6, node_2, node_8     # output 6
root, p, q = node_6, node_4, node_3     # output 6

test = Solution()
print(test.lowestCommonAncestor(root, p, q).val)

