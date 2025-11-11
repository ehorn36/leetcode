class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array,
        and return false if every element is distinct.

        length: 1 <= nums.length <= 105
        values: -10^9 <= nums[i] <= 10^9

        Idea here is to add each element to a hashmap. Every loop, check if the current element is already in the
        hashmap. If yes, then return True (there is a duplicate). If you get through the whole array and haven't found
        a duplicate, then return False.
        """

        hashmap = {}
        for num in nums:
            if num in hashmap:
                return True
            else:
                hashmap[num] = 1
        return False


# nums = [1,2,3,1]    # True
# nums = [1,2,3,4]    # False
# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]   # True
# nums = [1]  # False

test = Solution()
output = test.containsDuplicate(nums)
print(output)
