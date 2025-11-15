import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good_integer = ""
        
        for i in range(len(num) - 2):
            # Check if the current character and the next two characters are the same
            if num[i] == num[i+1] == num[i+2]:
                # Update max_good_integer if the current good integer is larger
                if num[i] > max_good_integer:
                    max_good_integer = num[i] * 3
        
        return max_good_integer

def largestGoodInteger(num: str) -> str:
    return Solution().largestGoodInteger(num)