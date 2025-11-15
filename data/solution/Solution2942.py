import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [index for index, word in enumerate(words) if x in word]

def findWordsContaining(words: List[str], x: str) -> List[int]:
    return Solution().findWordsContaining(words, x)