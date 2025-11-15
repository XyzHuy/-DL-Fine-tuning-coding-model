import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMaximalUncoveredRanges(self, n: int, ranges: List[List[int]]) -> List[List[int]]:
        # Sort the ranges by their start points
        ranges.sort()
        
        # Initialize the result list and the current end of the last covered range
        result = []
        current_end = -1
        
        # Iterate through the sorted ranges
        for start, end in ranges:
            # If there is a gap between the current end and the start of the next range
            if start > current_end + 1:
                # Add the uncovered range to the result
                result.append([current_end + 1, start - 1])
            
            # Update the current end to the maximum end of the overlapping ranges
            current_end = max(current_end, end)
        
        # If there is an uncovered range at the end of the array
        if current_end < n - 1:
            result.append([current_end + 1, n - 1])
        
        return result

def findMaximalUncoveredRanges(n: int, ranges: List[List[int]]) -> List[List[int]]:
    return Solution().findMaximalUncoveredRanges(n, ranges)