import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome_range(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Try skipping either the left or the right character
                return is_palindrome_range(left + 1, right) or is_palindrome_range(left, right - 1)
            left, right = left + 1, right - 1
        return True

def validPalindrome(s: str) -> bool:
    return Solution().validPalindrome(s)