import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumDeletions(self, s: str) -> int:
        # Initialize counters for 'a's to be deleted and 'b's encountered
        delete_a = 0
        count_b = 0
        
        # Iterate through each character in the string
        for char in s:
            if char == 'b':
                # Increment 'b' counter
                count_b += 1
            else:
                # For 'a', we have two choices: delete this 'a' or all previous 'b's
                # We take the minimum of the two
                delete_a = min(delete_a + 1, count_b)
        
        return delete_a

def minimumDeletions(s: str) -> int:
    return Solution().minimumDeletions(s)