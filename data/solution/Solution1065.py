import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        words = set(words)
        n = len(text)
        return sorted(
            [[i, j] for i in range(n) for j in range(i, n) if text[i : j + 1] in words]
        )

def indexPairs(text: str, words: List[str]) -> List[List[int]]:
    return Solution().indexPairs(text, words)