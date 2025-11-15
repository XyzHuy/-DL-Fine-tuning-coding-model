import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq
from collections import defaultdict

class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        
        # Build the graph
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append((scores[b], b))
            graph[b].append((scores[a], a))
        
        # Keep only the top 3 highest scoring neighbors for each node
        for node in graph:
            graph[node] = heapq.nlargest(3, graph[node])
        
        max_score = -1
        
        # Iterate over each edge as the middle edge of the sequence
        for a, b in edges:
            score_ab = scores[a] + scores[b]
            for score_c, c in graph[a]:
                for score_d, d in graph[b]:
                    # Ensure all four nodes are distinct
                    if c != b and d != a and c != d:
                        max_score = max(max_score, score_ab + score_c + score_d)
        
        return max_score

def maximumScore(scores: List[int], edges: List[List[int]]) -> int:
    return Solution().maximumScore(scores, edges)