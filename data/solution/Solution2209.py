import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        n = len(floor)
        
        # dp[i][j] will store the minimum number of white tiles visible
        # from the first i tiles using j carpets.
        dp = [[float('inf')] * (numCarpets + 1) for _ in range(n + 1)]
        
        # Base case: no tiles, no white tiles visible.
        for j in range(numCarpets + 1):
            dp[0][j] = 0
        
        # Fill the dp table.
        for i in range(1, n + 1):
            for j in range(numCarpets + 1):
                # Option 1: Do not use a carpet for the ith tile.
                dp[i][j] = dp[i - 1][j] + (floor[i - 1] == '1')
                
                # Option 2: Use a carpet for the ith tile.
                if j > 0:
                    # Cover the tiles from i-carpetLen+1 to i with a carpet.
                    dp[i][j] = min(dp[i][j], dp[max(0, i - carpetLen)][j - 1])
        
        # The answer is the minimum number of white tiles visible using all numCarpets carpets.
        return dp[n][numCarpets]

def minimumWhiteTiles(floor: str, numCarpets: int, carpetLen: int) -> int:
    return Solution().minimumWhiteTiles(floor, numCarpets, carpetLen)