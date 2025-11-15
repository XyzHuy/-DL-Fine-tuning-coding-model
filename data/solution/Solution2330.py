import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def makePalindrome(self, s: str) -> bool:
        # Initialize a counter for mismatched characters
        mismatch_count = 0
        
        # Use two pointers to compare characters from the start and end
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                mismatch_count += 1
                # If more than 2 mismatches are found, return False
                if mismatch_count > 2:
                    return False
            left += 1
            right -= 1
        
        # If there are 0, 1, or 2 mismatches, it's possible to make the string a palindrome
        return True

def makePalindrome(s: str) -> bool:
    return Solution().makePalindrome(s)