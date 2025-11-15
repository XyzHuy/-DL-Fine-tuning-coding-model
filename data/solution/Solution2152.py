import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import gcd
from collections import defaultdict

class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # Function to get the line equation in the form of (a, b, c) where ax + by = c
        def get_line(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            a = y2 - y1
            b = x1 - x2
            c = x2 * y1 - x1 * y2
            g = gcd(gcd(a, b), c)
            return (a // g, b // g, c // g)
        
        # Precompute all lines that can be formed by each pair of points
        lines = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                line = get_line(points[i], points[j])
                lines[line].add(i)
                lines[line].add(j)
        
        # Memoization dictionary
        memo = {}
        
        # Bitmask representing which points are covered
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0
            if mask in memo:
                return memo[mask]
            res = float('inf')
            # Try to add a line that covers at least one uncovered point
            for line, point_set in lines.items():
                new_mask = mask
                for point in point_set:
                    if not (new_mask & (1 << point)):
                        new_mask |= (1 << point)
                if new_mask != mask:
                    res = min(res, 1 + dp(new_mask))
            memo[mask] = res
            return res
        
        return dp(0)

def minimumLines(points: List[List[int]]) -> int:
    return Solution().minimumLines(points)