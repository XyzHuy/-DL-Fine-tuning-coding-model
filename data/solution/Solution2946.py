import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            if i % 2 == 0:
                # Even-indexed row: cyclically shift to the left
                shifted_row = mat[i][k % n:] + mat[i][:k % n]
            else:
                # Odd-indexed row: cyclically shift to the right
                shifted_row = mat[i][-k % n:] + mat[i][:-k % n]
            
            if shifted_row != mat[i]:
                return False
        
        return True

def areSimilar(mat: List[List[int]], k: int) -> bool:
    return Solution().areSimilar(mat, k)