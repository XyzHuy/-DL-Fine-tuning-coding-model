import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        # dp[i] will store the maximum energy we can gain starting from index i
        dp = [0] * n
        
        # Start filling dp from the last index to the first
        for i in range(n - 1, -1, -1):
            # If we can jump from this index, take the maximum energy we can get from the next jump
            if i + k < n:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]
        
        # The result is the maximum value in dp array, as we can start from any index
        return max(dp)

def maximumEnergy(energy: List[int], k: int) -> int:
    return Solution().maximumEnergy(energy, k)