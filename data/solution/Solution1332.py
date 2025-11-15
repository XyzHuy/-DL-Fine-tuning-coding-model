import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # If the string is already a palindrome, it can be removed in one step.
        if s == s[::-1]:
            return 1
        # If the string is not a palindrome, it can be removed in two steps:
        # First, remove all 'a's in one step, then all 'b's in another step, or vice versa.
        else:
            return 2

def removePalindromeSub(s: str) -> int:
    return Solution().removePalindromeSub(s)