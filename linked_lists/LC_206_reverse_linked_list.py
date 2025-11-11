"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        """
        Iterative Approach
        """
        # previous_node = None
        # current_node = head
        #
        # # Move along linked list and assign each node to point backwards
        # while current_node is not None:
        #
        #     # Temporarily store the next node
        #     next_node = current_node.next
        #
        #     # Update current node to point backwards
        #     current_node.next = previous_node
        #
        #     # Move previous node forwards
        #     previous_node = current_node
        #
        #     # Move current node forwards
        #     current_node = next_node
        #
        # # Return the last node (which is now the head since everything points backwards)
        # return previous_node

        """
        Recursive Approach
        """

        # Base case
        if head is None or head.next is None:
            return head

        # Call recursive function and store returned node
        returned_node = self.reverseList(head.next)

        # Set next node to point backwards to current node
        head.next.next = head   # (4.next.next == 5.next == None)

        # Set current node to point to null (So the base case will trigger)
        head.next = None

        return returned_node







node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

test = Solution()
test.reverseList(node1)
print()