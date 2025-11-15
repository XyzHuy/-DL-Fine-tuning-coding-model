import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return Solution().transpose(matrix)