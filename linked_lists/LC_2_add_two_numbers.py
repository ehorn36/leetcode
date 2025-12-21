"""
https://leetcode.com/problems/add-two-numbers/description/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        If you look at the example output, it's also in reverse order. The idea here is to add the digits from both
        lists at the same time, then add that value to a new node in a return list. If the value > 9, we need to track the
        carry value, just like handwritten math.

        Example: 342 + 465 = 807 -----> 3 4 2
                                        4 6 5
                                        _____
                                        8 0 7 <-- First sum

        #1 Sum = 7 ------------> Node == [7], carry = 0
        #2 Sum = 10 + carry ---> Node == [0], carry = 1
        #3 Sum = 7  + carry ---> Node == [8], carry = 0

    Output: [7, 0, 8]

    Example 2:
        Input: l1 = [0], l2 = [0]
        Output: [0]

    Example 3:
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current_node = dummy
        carry = 0

        # Traverse lists until all are empty:
        while l1 or l2 or carry:

            # If node is valid, assign val; else assign 0
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            # Add values together
            value = value1 + value2 + carry

            # Determine value and carry for new node
            carry = value // 10     # Ex. 15 // 10 --> 1
            value = value % 10      # Ex. 15 %  10 --> 5

            # Add node w/value to return list
            current_node.next = ListNode(value)

            # Move to next node in all lists
            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node6 = ListNode(1)
node7 = ListNode(2)
node8 = ListNode(3)
node9 = ListNode(4)
node10 = ListNode(5)

node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

test = Solution()
node = test.addTwoNumbers(node1, node6)
print(node.val)

