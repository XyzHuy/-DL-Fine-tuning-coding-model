import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def digitCount(self, num: str) -> bool:
        # Convert the string to a list of integers for easier manipulation
        num_list = [int(digit) for digit in num]
        
        # Check each index to see if the condition holds
        for i in range(len(num_list)):
            # Count occurrences of the digit i in the list
            if num_list.count(i) != num_list[i]:
                return False
        
        return True

def digitCount(num: str) -> bool:
    return Solution().digitCount(num)