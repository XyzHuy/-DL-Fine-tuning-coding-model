import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Count the number of '1's in the string
        count_ones = s.count('1')
        
        # If there is only one '1', it must be placed at the end
        if count_ones == 1:
            return '0' * (len(s) - 1) + '1'
        
        # Place all '1's except one at the beginning
        # Followed by all '0's
        # Place the last '1' at the end to ensure the number is odd
        return '1' * (count_ones - 1) + '0' * (len(s) - count_ones) + '1'

def maximumOddBinaryNumber(s: str) -> str:
    return Solution().maximumOddBinaryNumber(s)