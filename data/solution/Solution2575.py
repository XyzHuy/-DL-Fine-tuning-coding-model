import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        div = []
        remainder = 0
        for digit in word:
            remainder = (remainder * 10 + int(digit)) % m
            div.append(1 if remainder == 0 else 0)
        return div

def divisibilityArray(word: str, m: int) -> List[int]:
    return Solution().divisibilityArray(word, m)