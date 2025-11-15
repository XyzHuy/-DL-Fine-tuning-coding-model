import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        count = 0
        for i in points:
            dist_map = defaultdict(int)
            for j in points:
                dist_map[distance(i, j)] += 1
            for dist in dist_map:
                count += dist_map[dist] * (dist_map[dist] - 1)
        
        return count

def numberOfBoomerangs(points: List[List[int]]) -> int:
    return Solution().numberOfBoomerangs(points)