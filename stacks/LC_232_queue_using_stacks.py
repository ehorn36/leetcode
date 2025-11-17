"""
https://leetcode.com/problems/implement-queue-using-stacks/
"""

class MyQueue:
    """
    Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the
    functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:

        *   void push(int x) Pushes element x to the back of the queue.
        *   int pop() Removes the element from the front of the queue and returns it.
        *   int peek() Returns the element at the front of the queue.
        *   boolean empty() Returns true if the queue is empty, false otherwise.

    Notes:

        *   You must use only standard operations of a stack, which means only push to top, peek/pop from top, size,
            and is empty operations are valid.

        *   Depending on your language, the stack may not be supported natively. You may simulate a stack using a
            list or deque (double-ended queue) as long as you use only a stack's standard operations.
    """

    def __init__(self):
        self._queue = []

    # Add element to end of list
    def push(self, x: int) -> None:
        self._queue.append(x)

    # Return and remove element at front of list
    def pop(self) -> int:
        return self._queue.pop(0)

    # Return element at front of list
    def peek(self) -> int:
        return self._queue[0]

    # Returns True if list is empty, otherwise False
    def empty(self) -> bool:
        if len(self._queue) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()