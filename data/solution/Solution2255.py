import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if s.startswith(word):
                count += 1
        return count

def countPrefixes(words: List[str], s: str) -> int:
    return Solution().countPrefixes(words, s)