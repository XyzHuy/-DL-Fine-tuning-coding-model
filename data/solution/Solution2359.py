import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def find_distances(start):
            distances = [-1] * len(edges)
            current = start
            distance = 0
            while current != -1 and distances[current] == -1:
                distances[current] = distance
                current = edges[current]
                distance += 1
            return distances

        distances1 = find_distances(node1)
        distances2 = find_distances(node2)

        min_max_distance = float('inf')
        result_node = -1

        for i in range(len(edges)):
            if distances1[i] != -1 and distances2[i] != -1:
                max_distance = max(distances1[i], distances2[i])
                if max_distance < min_max_distance or (max_distance == min_max_distance and i < result_node):
                    min_max_distance = max_distance
                    result_node = i

        return result_node

def closestMeetingNode(edges: List[int], node1: int, node2: int) -> int:
    return Solution().closestMeetingNode(edges, node1, node2)