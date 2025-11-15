import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        
        # If it's impossible to merge into one pile, return -1
        if (n - 1) % (k - 1) != 0:
            return -1
        
        # Precompute prefix sums for quick range sum calculation
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stones[i]
        
        # Initialize the DP table with infinity
        dp = [[[float('inf')] * (k + 1) for _ in range(n)] for _ in range(n)]
        
        # Base case: merging a single pile into 1 pile costs 0
        for i in range(n):
            dp[i][i][1] = 0
        
        # Fill the DP table
        for length in range(2, n + 1):  # length of the subarray
            for i in range(n - length + 1):  # starting index of the subarray
                j = i + length - 1  # ending index of the subarray
                for m in range(2, k + 1):  # number of piles
                    if (j - i) % (k - 1) != (m - 1) % (k - 1):
                        continue
                    for mid in range(i, j, k - 1):  # split point
                        dp[i][j][m] = min(dp[i][j][m], dp[i][mid][1] + dp[mid + 1][j][m - 1])
                if (j - i) % (k - 1) == 0:
                    dp[i][j][1] = dp[i][j][k] + prefix_sum[j + 1] - prefix_sum[i]
        
        return dp[0][n - 1][1] if dp[0][n - 1][1] != float('inf') else -1

def mergeStones(stones: List[int], k: int) -> int:
    return Solution().mergeStones(stones, k)