import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        
        # Find the first digit that is not '9' for the maximum value
        for i, digit in enumerate(num_str):
            if digit != '9':
                max_value = int(num_str.replace(digit, '9'))
                break
        else:
            # If all digits are '9', the max value is the number itself
            max_value = num
        
        # Find the first digit to replace with '0' for the minimum value
        min_value = int(num_str.replace(num_str[0], '0'))
        
        return max_value - min_value

def minMaxDifference(num: int) -> int:
    return Solution().minMaxDifference(num)