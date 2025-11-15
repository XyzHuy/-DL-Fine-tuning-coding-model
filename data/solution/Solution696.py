import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # Initialize variables to keep track of the counts of consecutive 0's and 1's
        prev_count = 0
        current_count = 1
        result = 0
        
        # Iterate through the string starting from the second character
        for i in range(1, len(s)):
            # If the current character is the same as the previous one, increment the current count
            if s[i] == s[i - 1]:
                current_count += 1
            else:
                # Otherwise, add the minimum of the previous and current counts to the result
                result += min(prev_count, current_count)
                # Update the previous count to the current count
                prev_count = current_count
                # Reset the current count to 1
                current_count = 1
        
        # Add the last pair of counts to the result
        result += min(prev_count, current_count)
        
        return result

def countBinarySubstrings(s: str) -> int:
    return Solution().countBinarySubstrings(s)