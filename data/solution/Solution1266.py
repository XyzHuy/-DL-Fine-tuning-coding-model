import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        for i in range(1, len(points)):
            x_diff = abs(points[i][0] - points[i-1][0])
            y_diff = abs(points[i][1] - points[i-1][1])
            total_time += max(x_diff, y_diff)
        return total_time

def minTimeToVisitAllPoints(points: List[List[int]]) -> int:
    return Solution().minTimeToVisitAllPoints(points)