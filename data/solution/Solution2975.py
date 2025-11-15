import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        
        # Add the boundary fences
        hFences.extend([1, m])
        vFences.extend([1, n])
        
        # Sort the fences
        hFences.sort()
        vFences.sort()
        
        # Calculate all possible horizontal and vertical distances between fences
        h_distances = set()
        v_distances = set()
        
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_distances.add(abs(hFences[i] - hFences[j]))
        
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_distances.add(abs(vFences[i] - vFences[j]))
        
        # Find the maximum possible square area
        max_side = 0
        for side in h_distances:
            if side in v_distances:
                max_side = max(max_side, side)
        
        # Return the result
        if max_side == 0:
            return -1
        else:
            return (max_side ** 2) % MOD

def maximizeSquareArea(m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
    return Solution().maximizeSquareArea(m, n, hFences, vFences)