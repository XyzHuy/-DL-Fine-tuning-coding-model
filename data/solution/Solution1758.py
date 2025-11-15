import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minOperations(self, s: str) -> int:
        # We need to compare the string with two possible alternating patterns:
        # 1. Pattern starting with '0': "010101..."
        # 2. Pattern starting with '1': "101010..."
        
        # Initialize counters for the number of changes needed for each pattern
        changes_for_pattern1 = 0  # Changes needed for "010101..."
        changes_for_pattern2 = 0  # Changes needed for "101010..."
        
        # Iterate through the string and compare with both patterns
        for i, char in enumerate(s):
            if i % 2 == 0:
                # Even index: should be '0' for pattern1 and '1' for pattern2
                if char != '0':
                    changes_for_pattern1 += 1
                if char != '1':
                    changes_for_pattern2 += 1
            else:
                # Odd index: should be '1' for pattern1 and '0' for pattern2
                if char != '1':
                    changes_for_pattern1 += 1
                if char != '0':
                    changes_for_pattern2 += 1
        
        # The result is the minimum of the two counts
        return min(changes_for_pattern1, changes_for_pattern2)

def minOperations(s: str) -> int:
    return Solution().minOperations(s)