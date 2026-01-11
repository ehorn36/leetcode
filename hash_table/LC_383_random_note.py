"""
https://leetcode.com/problems/ransom-note/

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.

    Example 1:
        Input: ransomNote = "a", magazine = "b"
        Output: false

    Example 2:
        Input: ransomNote = "aa", magazine = "ab"
        Output: false

    Example 3:
        Input: ransomNote = "aa", magazine = "aab"
        Output: true

    Note:
        * Go through magazine and tally the letters in a hash table
        * Go through ransomNote and remove the letters from the hash table
        * If you run out of letters, then False, otherwise True
"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        hash_table = {}

        # Tally letters in hash_table
        for letter in magazine:
            if letter in hash_table:
                hash_table[letter] = hash_table[letter] + 1
            else:
                hash_table[letter] = 1

        # Remove the letters from the hash table
        for letter in ransomNote:

            # If letter not available to be removed, return False
            if letter not in hash_table or hash_table[letter] < 1:
                return False
            else:
                hash_table[letter] = hash_table[letter] - 1

        # If didn't return False, then all letters available
        return True