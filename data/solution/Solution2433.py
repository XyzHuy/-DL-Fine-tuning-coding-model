import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for i in range(1, len(pref)):
            arr.append(pref[i] ^ pref[i - 1])
        return arr

def findArray(pref: List[int]) -> List[int]:
    return Solution().findArray(pref)