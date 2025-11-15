import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        # Create a set to store all covered numbers
        covered_numbers = set()
        
        # Iterate over each range
        for start, end in ranges:
            # Add all numbers in the current range to the set
            covered_numbers.update(range(start, end + 1))
        
        # Check if all numbers from left to right are in the covered_numbers set
        for num in range(left, right + 1):
            if num not in covered_numbers:
                return False
        
        return True

def isCovered(ranges: List[List[int]], left: int, right: int) -> bool:
    return Solution().isCovered(ranges, left, right)