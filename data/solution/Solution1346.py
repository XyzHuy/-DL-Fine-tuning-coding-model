import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for x in arr:
            if x * 2 in s or (x % 2 == 0 and x // 2 in s):
                return True
            s.add(x)
        return False

def checkIfExist(arr: List[int]) -> bool:
    return Solution().checkIfExist(arr)