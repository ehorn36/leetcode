"""
https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Given an integer array nums, return an array answer such that answer[i] is equal to the product
        of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is
        guaranteed to fit in a 32-bit integer.You must write an algorithm that runs in O(n) time and
        without using the division operation.

        *** Things to observe ***
        * Can only find products in 1 pass.
        * Array is not sorted.
        * No division.
        * All products in the return array are going to be some fraction of the product of all numbers

        *** Idea / Trick ***
        1) Multiply each value within the input array from left to right, placing each product in the prefix array. Now,
        prefix_array[i] equals the product of all values that come before nums[i].

        2) Do the same thing, but from right to left, and place each product in the postfix array. Similarly, postfix[i]
        equals the product of all values that come after nums[i].

        3) Now that we have the product of numbers before and after nums[i],
        prefix[i] * postfix[i] == product of all the elements of nums except nums[i].


        Input array =                                  [ 1,    2,    3,    4   ]
        Product of all numbers to the left of i =   1, [ 1,    1*1,  2*1,  3*2 ]      ==  [1,  1,  2,  6]
        Product of all numbers to the right of i =     [ 2*12, 3*4,  4*1,  1   ], 1   ==  [24, 12, 4,  1]
        Answer                                                                        ==  [24, 12, 8,  6]

        Input array =                                  [ 2,    4,    3,    5   ]
        Product of all numbers to the left of i =   1, [ 1,    2*1,  4*2,  3*8 ]      ==  [1,  2,  8,  24]
        Product of all numbers to the right of i =     [ 4*15, 3*5,  5*1,  1   ], 1   ==  [60, 15, 5,  1 ]
        Answer                                                                        ==  [60, 30, 40, 24]

        """
        prefix_array = [1]
        postfix_array = [1]
        answer_array = []

        # Left products (prefix)
        for i in range(1, len(nums)):                           # 1 = start, len(nums) = stop
            product = nums[i - 1] * prefix_array[i - 1]
            prefix_array.append(product)

        # Right products (postfix)
        for j in range(len(nums) - 2, -1, -1):                  # Start at 2nd to last index, go until 0, move backwards
            product = nums[j + 1] * postfix_array[0]            # Since moving backwards, multiply value @ front of array
            postfix_array.insert(0, product)            # Insert product at front of list

        # Multiply prefix and postfix products together at for each i position
        for k in range(len(nums)):
            product = prefix_array[k] * postfix_array[k]
            answer_array.append(product)

        return answer_array


nums = [1, 2, 3, 4]               # [24,12,8,6]
# nums = [-1, 1, 0, -3, 3]          # [0,0,9,0,0]
# nums = [2, 4, 3, 5]               # [60, 30, 40, 24]

test = Solution()
print(test.productExceptSelf(nums))
