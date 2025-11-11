class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        return False

# s = "anagram"
# t = "nagaram"

# s = "rat"
# t = "car"

s = ""
t = ""

test = Solution()
print(test.isAnagram(s, t))