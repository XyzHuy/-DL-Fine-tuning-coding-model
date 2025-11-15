import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import inf

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        i = j = -1
        ans = inf
        for k, w in enumerate(wordsDict):
            if w == word1:
                i = k
            if w == word2:
                j = k
            if i != -1 and j != -1:
                ans = min(ans, abs(i - j))
        return ans

def shortestDistance(wordsDict: List[str], word1: str, word2: str) -> int:
    return Solution().shortestDistance(wordsDict, word1, word2)