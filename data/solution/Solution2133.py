import random
import functools
import collections
import string
import math
import datetime


from itertools import chain
from typing import List

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        return all(len(set(row)) == n for row in chain(matrix, zip(*matrix)))

def checkValid(matrix: List[List[int]]) -> bool:
    return Solution().checkValid(matrix)