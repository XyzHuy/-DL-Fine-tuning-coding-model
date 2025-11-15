import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        score = [0] * n
        
        # Calculate the edge scores
        for i, edge in enumerate(edges):
            score[edge] += i
        
        # Find the node with the highest edge score
        max_score = max(score)
        for i in range(n):
            if score[i] == max_score:
                return i

def edgeScore(edges: List[int]) -> int:
    return Solution().edgeScore(edges)