import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Helper function to find the longest palindromic prefix
        def longest_palindromic_prefix(s):
            n = len(s)
            rev_s = s[::-1]
            # Create a new string which is s + '#' + reverse of s
            new_s = s + '#' + rev_s
            # Create a LPS (Longest Prefix Suffix) array
            lps = [0] * len(new_s)
            # Build the LPS array
            for i in range(1, len(new_s)):
                j = lps[i - 1]
                while j > 0 and new_s[i] != new_s[j]:
                    j = lps[j - 1]
                if new_s[i] == new_s[j]:
                    j += 1
                lps[i] = j
            # The length of the longest palindromic prefix
            return lps[-1]
        
        # Find the longest palindromic prefix
        lpp_length = longest_palindromic_prefix(s)
        # Characters to add in front to make the whole string a palindrome
        to_add = s[lpp_length:][::-1]
        # Return the shortest palindrome
        return to_add + s

def shortestPalindrome(s: str) -> str:
    return Solution().shortestPalindrome(s)