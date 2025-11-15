import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Calculate the degree (number of connections) for each city
        degree = [0] * n
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
        
        # Sort cities based on their degree in ascending order
        degree.sort()
        
        # Assign the smallest number to the city with the smallest degree
        # and the largest number to the city with the largest degree
        total_importance = sum(degree[i] * (i + 1) for i in range(n))
        
        return total_importance

def maximumImportance(n: int, roads: List[List[int]]) -> int:
    return Solution().maximumImportance(n, roads)