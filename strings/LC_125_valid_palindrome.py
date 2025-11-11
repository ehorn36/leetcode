class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
        non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters
        and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

        Example 1:

            Input: s = "A man, a plan, a canal: Panama"
            Output: true
            Explanation: "amanaplanacanalpanama" is a palindrome.

        Example 2:

            Input: s = "race a car"
            Output: false
            Explanation: "raceacar" is not a palindrome.

        Example 3:

            Input: s = " "
            Output: true
            Explanation: s is an empty string "" after removing non-alphanumeric characters.
            Since an empty string reads the same forward and backward, it is a palindrome.

        """

        left = 0
        right = len(s) - 1

        # double pointer
        while left < right:

            # Skip left pointer past non-alphanum characters
            while left < right and not self.isalphanum(s[left]):
                left += 1

            # Skip right pointer past non-alphanum characters
            while right > left and not self.isalphanum(s[right]):
                right -= 1

            # Once pointers in position, check values
            if s[left].upper() != s[right].upper():
                return False

            # Move pointers to next values
            left += 1
            right -= 1

        # If didn't return False, then must be True.
        return True

    # Helper function. Similar to Python's isalnum()
    def isalphanum(self, char) -> bool:
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))



s = "A man, a plan, a canal: Panama"        # True
# s = "race a car"                            # False
# s = " "                                     # True
# s = "0P"                                    # False

test = Solution()
print(test.isPalindrome(s))
