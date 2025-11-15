import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minSwaps(self, s: str) -> int:
        # Count the number of '0's and '1's in the string
        count_0 = s.count('0')
        count_1 = s.count('1')
        
        # If the difference between the counts of '0's and '1's is more than 1, it's impossible to make the string alternating
        if abs(count_0 - count_1) > 1:
            return -1
        
        # Helper function to calculate the number of swaps needed to match the pattern
        def calculate_swaps(pattern):
            swaps = 0
            for i in range(len(s)):
                if s[i] != pattern[i]:
                    swaps += 1
            return swaps // 2  # Each swap fixes two positions
        
        # Determine the possible alternating patterns
        if count_0 > count_1:
            # Pattern starts with '0'
            pattern = '01' * (len(s) // 2) + '0'
        elif count_1 > count_0:
            # Pattern starts with '1'
            pattern = '10' * (len(s) // 2) + '1'
        else:
            # Two possible patterns: starting with '0' or '1'
            pattern1 = '01' * (len(s) // 2)
            pattern2 = '10' * (len(s) // 2)
            return min(calculate_swaps(pattern1), calculate_swaps(pattern2))
        
        # Calculate and return the number of swaps needed for the determined pattern
        return calculate_swaps(pattern)

def minSwaps(s: str) -> int:
    return Solution().minSwaps(s)