class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets
        array length >= 3
        array values - & +

        We need to find 3 unique elements whose value adds to 0. We can't use the same element
        more than once per triplet, triplets must not be duplicates of each other, and all 3 values must equal zero.
        Since there are duplicate values in the input array, this means that if you triple loop to brute force
        your way through the input array, there will be duplicate triplets (e.g. [1, 1, 0, -1] == [1, 0, -1] x 2)

        The idea here is to break the algorithm into two parts: iterating through the input array once while avoiding
        duplicates + finding the remaining two values that result in a sum of 0 using a double pointer
        (similar to twoSum II). In order to use pointers, the array must be sorted!

        """
        return_array = []

        nums.sort()

        # Iterate once through sorted list
        for i in range(len(nums)):

            # If the current and previous value are the same, then skip element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use pointers to locate values
            left_ptr = i + 1
            right_ptr = len(nums) - 1

            # Loop until left_ptr crosses right_ptr
            while left_ptr < right_ptr:
                three_sum = nums[i] + nums[left_ptr] + nums[right_ptr]

                # If number too high, move right pointer to the left to decrease the value
                if three_sum > 0:
                    right_ptr -= 1

                # If number too low, move left pointer to the right to increase the value
                elif three_sum < 0:
                    left_ptr += 1

                # Found three_sum
                else:

                    # Add triplet to array
                    triplet = [nums[i], nums[left_ptr], nums[right_ptr]]
                    return_array.append(triplet)

                    # Move either pointer (left in this case) to point to the next unique value. Don't cross other ptr!
                    # This will cause three_sum to change its value, which causes the while loop to reactivate
                    # The new value will either be too high, low, or 0.
                    left_ptr += 1
                    while nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr:
                        left_ptr += 1

        return return_array














nums = [-1, 0, 1, 2, -1, -4]    # [[-1,-1,2],[-1,0,1]]
# nums = [0, 1, 1]                # []
# nums = [0, 0, 0]                # [[0,0,0]]

test = Solution()
output = test.threeSum(nums)
print(output)
