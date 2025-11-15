import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        # In each operation, we can increase num by 1 and decrease x by 1,
        # effectively increasing the difference between num and x by 2.
        # Therefore, the maximum achievable value of x is num + 2*t.
        return num + 2 * t

def theMaximumAchievableX(num: int, t: int) -> int:
    return Solution().theMaximumAchievableX(num, t)