import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        for interval in intervals:
            left, right = interval
            # If the interval is completely before toBeRemoved or completely after
            if right <= toBeRemoved[0] or left >= toBeRemoved[1]:
                result.append(interval)
            else:
                # If there's a part of the interval before toBeRemoved
                if left < toBeRemoved[0]:
                    result.append([left, toBeRemoved[0]])
                # If there's a part of the interval after toBeRemoved
                if right > toBeRemoved[1]:
                    result.append([toBeRemoved[1], right])
        return result

def removeInterval(intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
    return Solution().removeInterval(intervals, toBeRemoved)