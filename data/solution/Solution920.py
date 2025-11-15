import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i][j] will store the number of ways to create a playlist of length i with j different songs
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        
        # Base case: one way to create a playlist of length 0 with 0 songs
        dp[0][0] = 1
        
        for i in range(1, goal + 1):
            for j in range(1, n + 1):
                # Case 1: We add a new song to the playlist
                dp[i][j] = dp[i - 1][j - 1] * (n - (j - 1))
                
                # Case 2: We replay a song that was played at least k songs ago
                if j > k:
                    dp[i][j] += dp[i - 1][j] * (j - k)
                
                dp[i][j] %= MOD
        
        return dp[goal][n]

def numMusicPlaylists(n: int, goal: int, k: int) -> int:
    return Solution().numMusicPlaylists(n, goal, k)