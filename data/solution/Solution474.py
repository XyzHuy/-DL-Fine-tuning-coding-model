import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Create a 3D DP array with dimensions (len(strs) + 1) x (m + 1) x (n + 1)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        
        # Iterate over each string in strs
        for i in range(1, len(strs) + 1):
            # Count the number of 0's and 1's in the current string
            zeros = strs[i - 1].count('0')
            ones = strs[i - 1].count('1')
            
            # Update the DP array
            for j in range(m + 1):
                for k in range(n + 1):
                    # If the current string can be included in the subset
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zeros][k - ones] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        
        # The answer is the maximum size of the subset with at most m 0's and n 1's
        return dp[len(strs)][m][n]

def findMaxForm(strs: List[str], m: int, n: int) -> int:
    return Solution().findMaxForm(strs, m, n)