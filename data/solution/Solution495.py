import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        
        total_poisoned_time = 0
        for i in range(1, len(timeSeries)):
            # Calculate the overlap between the current and previous poison durations
            overlap = min(duration, timeSeries[i] - timeSeries[i - 1])
            total_poisoned_time += overlap
        
        # Add the duration for the last attack, as it will fully contribute to the poisoned time
        total_poisoned_time += duration
        
        return total_poisoned_time

def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    return Solution().findPoisonedDuration(timeSeries, duration)