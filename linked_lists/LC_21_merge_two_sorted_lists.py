"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""

"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

Example 2:
    Input: list1 = [], list2 = []
    Output: []

Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Create fake head
        dummy_node = ListNode()

        # Start linked list, beginning with dummy node
        current_node = dummy_node

        # Loop through both lists until a .next is invalid
        while list1 and list2:

            # If node1 < node2
            if list1.val < list2.val:

                # Attach node1 to the list
                current_node.next = list1

                # Then, update the current node to be the one you just attached
                current_node = list1

                # Move list1 to point at the next node in the list
                list1 = list1.next

            else:

                # Otherwise, attached node2 to the list
                current_node.next = list2

                # Then, update the current node to be the one you just attached
                current_node = list2

                # Move list2 to point at the next node in the list
                list2 = list2.next

        # If either list1 or list2 has something remaining, add it to the list.
        current_node.next = list1 if list1 else list2

        # The list started with a dummy head, so return the second node (and subsequent list)
        return dummy_node.next




