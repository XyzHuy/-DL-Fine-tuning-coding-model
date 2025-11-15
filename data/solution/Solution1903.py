import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Iterate over the string from the end to the beginning
        for i in range(len(num) - 1, -1, -1):
            # Check if the current digit is odd
            if int(num[i]) % 2 != 0:
                # Return the substring from the start to the current position (inclusive)
                return num[:i+1]
        # If no odd digit is found, return an empty string
        return ""

def largestOddNumber(num: str) -> str:
    return Solution().largestOddNumber(num)