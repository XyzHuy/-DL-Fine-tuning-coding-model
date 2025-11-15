import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        province_count = 0

        for city in range(n):
            if not visited[city]:
                dfs(city)
                province_count += 1

        return province_count

def findCircleNum(isConnected: List[List[int]]) -> int:
    return Solution().findCircleNum(isConnected)