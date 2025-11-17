"""
https://leetcode.com/problems/binary-search/description/
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
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1

            # Middle must == target
            else:
                return middle

        # If target not found
        return -1


nums = [0, 1, 2, 3, 4]
target = 1

test = Solution()
print(test.search(nums, target))
