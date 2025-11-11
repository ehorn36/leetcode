class Solution:
    def twoSum(self, nums: list, target: int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        index1 = 0
        index2 = index1 + 1

        for num1 in range(len(nums) - 1):
            for num2 in range(len(nums) - index1 - 1):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]
                else:
                    index2 += 1
            index1 += 1
            index2 = index1 + 1




# array = [-1, -2, -3, -4, -5]
# target_num = -8

# array = [2,2,11,7]
# target_num = 9
#
array = [3,3]
target_num = 6


array = [-1,-2,-3,-4,-5]
target_num = -8

output = Solution().twoSum(array, target_num)

print(output)