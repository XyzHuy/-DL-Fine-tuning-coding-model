import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def magicalString(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 3:
            return 1
        
        # Initialize the magical string with the first few elements
        s = [1, 2, 2]
        i = 2  # The position in s that indicates the length of the next group
        
        while len(s) < n:
            next_num = 3 - s[-1]  # Determine the next number to add (1 or 2)
            next_count = s[i]  # Determine how many times the next number should be added
            
            # Extend the magical string by adding the next number the required number of times
            s.extend([next_num] * next_count)
            
            i += 1  # Move to the next position in s
        
        # Return the count of 1's in the first n elements of the magical string
        return s[:n].count(1)

def magicalString(n: int) -> int:
    return Solution().magicalString(n)