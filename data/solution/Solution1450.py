import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime <= end:
                count += 1
        return count

def busyStudent(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    return Solution().busyStudent(startTime, endTime, queryTime)