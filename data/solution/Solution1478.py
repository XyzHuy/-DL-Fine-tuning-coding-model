import random
import functools
import collections
import string
import math
import datetime


from typing import List
from functools import lru_cache

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()  # Sort the houses to facilitate distance calculations

        @lru_cache(None)
        def cost(i, j):  # Calculate the minimum cost to place one mailbox for houses[i:j+1]
            if i == j:
                return 0
            if i + 1 == j:
                return houses[j] - houses[i]
            return cost(i + 1, j - 1) + houses[j] - houses[i]

        @lru_cache(None)
        def dp(n, m):  # Minimum distance for n houses and m mailboxes
            if n == m:
                return 0
            if m == 1:
                return cost(0, n - 1)
            return min(dp(i, m - 1) + cost(i, n - 1) for i in range(m - 1, n))

        return dp(len(houses), k)

def minDistance(houses: List[int], k: int) -> int:
    return Solution().minDistance(houses, k)