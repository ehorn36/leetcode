"""
https://leetcode.com/problems/sort-colors/
"""

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the
        same color are adjacent, with the colors in the order red, white, and blue. We will use the integers 0, 1, and 2
        to represent the color red, white, and blue, respectively. You must solve this problem without using the
        library's sort function.

        Constraints:

            n == nums.length
            1 <= n <= 300   (1 - 300 elements)
            nums[i] is either 0, 1, or 2 (elements are either 1, 2, or 3)



        """
        index_of_2 = len(nums)
        i = 0

        # Loop through list once
        for num in range(len(nums)):

            # If 0, remove and insert at front of list, increment index by 1.
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1

            # If 2, remove and append to end of list, do not increment index
            elif nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                index_of_2 -= 1

            # Otherwise, i == 1, so just look at next item in array
            else:
                i += 1


test = Solution()

# nums = [2, 0, 2, 1, 1, 0]   # Output: [0,0,1,1,2,2]
# nums = [2, 0, 1]            # Output: [0,1,2]
# nums = [1, 0, 0]            # Output: [0,0,1]
nums = [1, 2]  # Output: [1, 2]

test.sortColors(nums)
print(nums)
