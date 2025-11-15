import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_left

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full_lakes = {}  # Dictionary to store the last day each lake was filled
        dry_days = []  # List to store the days we can dry a lake
        result = [-1] * len(rains)  # Initialize the result array with -1
        
        for i, rain in enumerate(rains):
            if rain == 0:
                # If it's a dry day, store the day in dry_days
                dry_days.append(i)
                result[i] = 1  # Default to drying an arbitrary lake, can be changed later
            else:
                if rain in full_lakes:
                    # If the lake is already full, find a dry day to empty it
                    dry_day_index = bisect_left(dry_days, full_lakes[rain])
                    if dry_day_index >= len(dry_days):
                        # If no dry day is available to empty the lake, return an empty array
                        return []
                    # Use the dry day to empty the lake
                    result[dry_days.pop(dry_day_index)] = rain
                # Mark the lake as full on this day
                full_lakes[rain] = i
        
        return result

def avoidFlood(rains: List[int]) -> List[int]:
    return Solution().avoidFlood(rains)