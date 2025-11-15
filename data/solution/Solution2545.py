import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # Sort the rows of the matrix based on the k-th column in descending order
        return sorted(score, key=lambda x: x[k], reverse=True)

def sortTheStudents(score: List[List[int]], k: int) -> List[List[int]]:
    return Solution().sortTheStudents(score, k)