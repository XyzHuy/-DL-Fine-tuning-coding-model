import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Sort each cuboid's dimensions
        for cuboid in cuboids:
            cuboid.sort()
        
        # Sort all cuboids
        cuboids.sort()
        
        n = len(cuboids)
        # dp[i] will be the maximum height we can achieve with cuboid i at the bottom
        dp = [0] * n
        
        for i in range(n):
            # The minimum height is the height of the cuboid itself
            dp[i] = cuboids[i][2]
            for j in range(i):
                # Check if cuboid j can be placed on cuboid i
                if (cuboids[j][0] <= cuboids[i][0] and 
                    cuboids[j][1] <= cuboids[i][1] and 
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
        
        # The result is the maximum value in dp array
        return max(dp)

def maxHeight(cuboids: List[List[int]]) -> int:
    return Solution().maxHeight(cuboids)