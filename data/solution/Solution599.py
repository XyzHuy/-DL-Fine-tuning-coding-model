import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import inf

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {s: i for i, s in enumerate(list2)}
        ans = []
        mi = inf
        for i, s in enumerate(list1):
            if s in d:
                j = d[s]
                if i + j < mi:
                    mi = i + j
                    ans = [s]
                elif i + j == mi:
                    ans.append(s)
        return ans

def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
    return Solution().findRestaurant(list1, list2)