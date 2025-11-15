import random
import functools
import collections
import string
import math
import datetime


from typing import List
from bisect import bisect_right

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect_right(letters, target)
        return letters[i % len(letters)]

def nextGreatestLetter(letters: List[str], target: str) -> str:
    return Solution().nextGreatestLetter(letters, target)