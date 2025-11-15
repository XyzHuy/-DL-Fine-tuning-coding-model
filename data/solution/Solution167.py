import random
import functools
import collections
import string
import math
import datetime


from bisect import bisect_left
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            x = target - numbers[i]
            j = bisect_left(numbers, x, lo=i + 1)
            if j < n and numbers[j] == x:
                return [i + 1, j + 1]

def twoSum(numbers: List[int], target: int) -> List[int]:
    return Solution().twoSum(numbers, target)