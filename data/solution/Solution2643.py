import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones_count = -1
        result_row_index = -1
        
        for i, row in enumerate(mat):
            ones_count = row.count(1)
            if ones_count > max_ones_count:
                max_ones_count = ones_count
                result_row_index = i
        
        return [result_row_index, max_ones_count]

def rowAndMaximumOnes(mat: List[List[int]]) -> List[int]:
    return Solution().rowAndMaximumOnes(mat)