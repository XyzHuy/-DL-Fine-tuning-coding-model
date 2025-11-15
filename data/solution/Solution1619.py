import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        n = len(arr)
        start, end = int(n * 0.05), int(n * 0.95)
        arr.sort()
        t = arr[start:end]
        return round(sum(t) / len(t), 5)

def trimMean(arr: List[int]) -> float:
    return Solution().trimMean(arr)