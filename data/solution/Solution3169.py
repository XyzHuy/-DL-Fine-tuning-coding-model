import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Merge overlapping intervals
        meetings.sort()
        merged_meetings = []
        
        for meeting in meetings:
            if not merged_meetings or merged_meetings[-1][1] < meeting[0] - 1:
                merged_meetings.append(meeting)
            else:
                merged_meetings[-1][1] = max(merged_meetings[-1][1], meeting[1])
        
        # Calculate available days
        available_days = days
        for start, end in merged_meetings:
            available_days -= (end - start + 1)
        
        return available_days

def countDays(days: int, meetings: List[List[int]]) -> int:
    return Solution().countDays(days, meetings)