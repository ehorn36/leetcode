"""
https://leetcode.com/problems/binary-search/description/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to
search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

Constraints:
   * 1 <= nums.length <= 10^4
   * -10^4 < nums[i], target < 10^4
   * All the integers in nums are unique.
   * nums is sorted in ascending order.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Set two pointers
        left = 0
        right = len(nums) - 1

        # Continue until left pointer cross right pointer
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] > target:

                # Keep left pointer the same and update right pointer to element before middle
                right = middle - 1

            elif nums[middle] < target:

                # Keep right pointer the same and update left pointer to element after middle
                left = middle + 1

            # Middle == target
            else:
                return middle

        # If target not found
        return -1


nums = [0, 1, 2, 3, 4]
target = 1

test = Solution()
print(test.search(nums, target))
