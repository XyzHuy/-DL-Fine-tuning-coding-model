import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # Create a set to store unique points covered by any car
        covered_points = set()
        
        # Iterate through each car's range
        for start, end in nums:
            # Add all points from start to end (inclusive) to the set
            for point in range(start, end + 1):
                covered_points.add(point)
        
        # The number of unique points is the size of the set
        return len(covered_points)

def numberOfPoints(nums: List[List[int]]) -> int:
    return Solution().numberOfPoints(nums)