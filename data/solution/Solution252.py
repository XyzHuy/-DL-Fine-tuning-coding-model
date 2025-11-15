import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        # Check if there is any overlap between consecutive intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        
        return True

def canAttendMeetings(intervals: List[List[int]]) -> bool:
    return Solution().canAttendMeetings(intervals)