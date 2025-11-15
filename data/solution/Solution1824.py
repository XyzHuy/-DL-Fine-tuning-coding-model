import random
import functools
import collections
import string
import math
import datetime


from typing import List
import math

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        # Initialize the minimum side jumps required to reach each lane at the starting point
        # Starting at lane 2, so initially, side jumps to reach lane 1 and lane 3 are 1 each
        dp = [1, 0, 1]  # dp[0] is lane 1, dp[1] is lane 2, dp[2] is lane 3
        
        for i in range(1, len(obstacles)):
            # If there's an obstacle in a lane, set the side jumps to infinity for that lane
            new_dp = [math.inf if obstacles[i] == j + 1 else dp[j] for j in range(3)]
            
            # Update the side jumps for each lane considering possible side jumps
            for j in range(3):
                if obstacles[i] != j + 1:
                    for k in range(3):
                        if j != k and obstacles[i] != k + 1:
                            new_dp[j] = min(new_dp[j], new_dp[k] + 1)
            
            dp = new_dp
        
        # Return the minimum side jumps required to reach any lane at the end point
        return min(dp)

def minSideJumps(obstacles: List[int]) -> int:
    return Solution().minSideJumps(obstacles)