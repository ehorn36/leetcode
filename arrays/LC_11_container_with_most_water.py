"""
https://leetcode.com/problems/container-with-most-water/
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
        of the ith line are (i, 0) and (i, height[i]). Find two lines that together with the x-axis form a container,
        such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.

        *** Eric's Notes ***
        The optimal solution involves using left and right pointers, starting at the outer edges of the array.
        First calculate the current area. If the current area is larger than max_area, update max_area.

        Next, move the pointer with the smaller value, since that value dictates the overall height (if we move the
        pointer with the larger value, the height would stay the same (dictated by the smaller value), unless it moves
        to a value smaller than the smaller value...which would result in an even smaller area).

        Continue this process until the pointers cross, then return max_area.
        """

        left_ptr = 0
        right_ptr = len(height) - 1
        max_area = 0

        while left_ptr < right_ptr:

            # Calculate current area and update max_area if larger
            min_height = min(height[left_ptr], height[right_ptr])
            length = right_ptr - left_ptr
            max_area = max(max_area, min_height * length)

            # If left pointer is smaller than right
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1

            # If right pointer is smaller than left
            else:
                right_ptr -= 1

        return max_area

test = Solution()

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # Output: 49

# height = [1, 1]  # Output: 1

# height = [0, 0]  # Output: 0
# height = [0, 1]  # Output: 0
# height = [1, 1, 1]  # Output: 2
height = [1, 5666, 5666, 1]  # Output: 2

print(test.maxArea(height))
