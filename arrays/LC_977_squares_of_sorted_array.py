"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/

Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Must be done in O(n) time

    Example 1:
        Input: nums = [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        Explanation: After squaring, the array becomes [16,1,0,9,100].
        After sorting, it becomes [0,1,9,16,100].

    Example 2:
        Input: nums = [-7,-3,2,3,11]
        Output: [4,9,9,49,121]

Note:
    * The farther away from zero (pos or neg), the larger the result of squaring a number.
    * Since this array is sorted, use left / right pointers and insert the largest of the numbers into
      the front of return array.
"""


class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = 0
        right = len(nums) - 1
        array = []

        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                array.insert(0, nums[left] ** 2)
                left += 1
            else:
                array.insert(0, nums[right] ** 2)
                right -= 1

        return array

nums = [-4, -1, 0, 3, 10]
test = Solution()
print(test.sortedSquares(nums))
