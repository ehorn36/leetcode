class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        """
        The idea here is that there is only 1 majority element, and it always exists. Once you find it, you're done!

        Iterate through nums and store the number in a hash map (dictionary), The key will be the number, and the value
        will be the count of times it's been found in nums. If the count is > (len(nums) / 2), boom you're done!
        """

        # Store values in dictionary (aka hash map)
        count_dict = {}
        for num in nums:

            # Increment current value in dictionary by + 1
            count_dict[num] = 1 + count_dict.get(num, 0)     # get num, otherwise return 0

            # Check if count > (len(nums) / 2)
            if count_dict[num] > (len(nums) / 2):
                return num

test = Solution()

# num_list = [3, 2, 3]
num_list = [2, 2, 1, 1, 1, 2, 2]

output = test.majorityElement(num_list)
print(output)
