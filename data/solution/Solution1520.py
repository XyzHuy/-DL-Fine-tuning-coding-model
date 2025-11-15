import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # Step 1: Find the first and last occurrence of each character
        first = {}
        last = {}
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
        
        # Step 2: Find the valid substrings
        intervals = []
        for char in first:
            start = first[char]
            end = last[char]
            j = start
            # Expand the interval to include all characters within the range
            while j <= end:
                if first[s[j]] < start:
                    break
                end = max(end, last[s[j]])
                j += 1
            else:
                intervals.append((start, end))
        
        # Step 3: Sort intervals by their end position
        intervals.sort(key=lambda x: x[1])
        
        # Step 4: Select non-overlapping intervals
        result = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                result.append(s[start:end+1])
                prev_end = end
        
        return result

def maxNumOfSubstrings(s: str) -> List[str]:
    return Solution().maxNumOfSubstrings(s)