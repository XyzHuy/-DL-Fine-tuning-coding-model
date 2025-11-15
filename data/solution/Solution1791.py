import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # In a star graph, the center node will be the only node that appears in every edge.
        # We can find the center by simply checking the first two edges.
        # The center node must be the common node in the first two edges.
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

def findCenter(edges: List[List[int]]) -> int:
    return Solution().findCenter(edges)