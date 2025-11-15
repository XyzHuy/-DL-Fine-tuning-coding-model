import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        n = len(arr)
        # dp[i][j] will be the minimum number of moves needed to remove the subarray arr[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single element subarrays
        for i in range(n):
            dp[i][i] = 1
        
        # Fill the table
        for length in range(2, n + 1):  # length of the subarray
            for i in range(n - length + 1):
                j = i + length - 1
                if length == 2:
                    dp[i][j] = 1 if arr[i] == arr[j] else 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] if arr[i] == arr[j] else float('inf')
                    for k in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        
        return dp[0][n - 1]

def minimumMoves(arr: List[int]) -> int:
    return Solution().minimumMoves(arr)