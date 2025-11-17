"""
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        """
        Things to note: There is only 1 solution, and you can't use the same element twice. If [3, 2, 4] and target is 6,
        you can't use 3 + 3 = 6, since you've used 3 twice. Also, the output is the index location, not the number, so
        you can't sort the array, otherwise the index will be different.

        Brute force way is to iterate through array N * N until you find a solution.

        Better way is to use a hash map. Iterate through array. Every element you encounter add to hash map.
        The target number - the current element == X? If X was previously added to the hashmap, then you've
        found the two elements that sum to two_sum.

        Since you only go through the array once, you don't have to worry about using the same element twice.
        Checking hashmap is O(1) time, so in total it's O(N) time to loop through array.
        """

        hashmap = {}            # key = number, value = index location
        for i in range(len(nums)):

            # Determine if needed number has previously been added to hashmap
            difference = target - nums[i]
            if difference in hashmap:
                return [i, hashmap[difference]]

            # Otherwise, add current num's index to hashmap
            hashmap[nums[i]] = i




test_nums = [2, 7, 11, 15]
test_target = 9

# test_nums = [3, 2, 4]
# test_target = 6

# test_nums = [3, 3]
# test_target = 6

# test_nums = [3, 2, 3]
# test_target = 6


test = Solution()
output = test.twoSum(test_nums, test_target)
print(output)



