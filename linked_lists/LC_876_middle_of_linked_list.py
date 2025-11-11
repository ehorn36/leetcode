# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example1:

    Input: head = [1,2,3,4,5]
    Output: [3,4,5]
    Explanation: The middle node of the list is node 3.

Example2:

    Input: head = [1,2,3,4,5,6]
    Output: [4,5,6]
    Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
    The number of nodes in the list is in the range [1, 100].
    1 <= Node.val <= 100
"""


class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        '''
        Easy way
        '''
        # length = 1
        # current_node = head
        # middle = None
        #
        # while current_node.next:
        #     current_node = current_node.next
        #     length += 1
        #
        # # If even number of nodes
        # if length % 2 == 0:
        #     middle = (length / 2) + 1
        #
        # # If odd number of nodes
        # else:
        #     middle = (length // 2) + 1
        #
        # current_node = head
        # runner = 1
        # while runner < middle:
        #     current_node = current_node.next
        #     runner += 1
        #
        # return current_node

        '''
        Slow / Fast algorithm
        Fast moves 2x faster than slow, therefore slow is always 'middle'
        '''

        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow



node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

test = Solution()
node = test.middleNode(node1)
print(node.val)



