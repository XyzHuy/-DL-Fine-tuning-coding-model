import random
import functools
import collections
import string
import math
import datetime


from math import comb
from typing import List

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        v, h = destination
        path = []
        total_moves = v + h
        
        for total in range(total_moves, 0, -1):
            if h > 0:
                # Calculate the number of paths if we take 'H' now
                paths_with_H = comb(total - 1, h - 1)
                if k <= paths_with_H:
                    path.append('H')
                    h -= 1
                else:
                    path.append('V')
                    k -= paths_with_H
                    v -= 1
            else:
                # If no more 'H' moves are left, we must take 'V'
                path.append('V')
                v -= 1
        
        return ''.join(path)

def kthSmallestPath(destination: List[int], k: int) -> str:
    return Solution().kthSmallestPath(destination, k)