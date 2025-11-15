import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(1 for hour in hours if hour >= target)

def numberOfEmployeesWhoMetTarget(hours: List[int], target: int) -> int:
    return Solution().numberOfEmployeesWhoMetTarget(hours, target)