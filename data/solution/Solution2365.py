import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_completed = {}
        days = 0
        
        for task in tasks:
            if task in last_completed:
                # Calculate the next available day for this task
                next_available_day = last_completed[task] + space + 1
                if days < next_available_day:
                    days = next_available_day
            # Complete the task on the current day
            last_completed[task] = days
            days += 1
        
        return days

def taskSchedulerII(tasks: List[int], space: int) -> int:
    return Solution().taskSchedulerII(tasks, space)