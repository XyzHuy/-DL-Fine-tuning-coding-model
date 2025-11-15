import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # Calculate the Manhattan distance between each worker and each bike
        distances = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, i, j))
        
        # Sort the distances by distance, then by worker index, then by bike index
        distances.sort()
        
        # Initialize result and used bike set
        result = [-1] * len(workers)
        used_bikes = set()
        
        # Assign bikes to workers based on sorted distances
        for distance, i, j in distances:
            if result[i] == -1 and j not in used_bikes:
                result[i] = j
                used_bikes.add(j)
        
        return result

def assignBikes(workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
    return Solution().assignBikes(workers, bikes)