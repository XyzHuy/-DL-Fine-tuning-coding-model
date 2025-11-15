import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # Count the frequency of each power value
        power_count = Counter(power)
        # Get the unique power values and sort them
        unique_powers = sorted(power_count.keys())
        
        # Initialize DP array
        dp = [0] * (len(unique_powers) + 1)
        
        # Fill the DP array
        for i in range(1, len(unique_powers) + 1):
            current_power = unique_powers[i - 1]
            # Option 1: Do not take any spell with power current_power
            dp[i] = dp[i - 1]
            # Option 2: Take all spells with power current_power
            # We need to ensure that we do not take any spells with power current_power - 1, current_power - 2, current_power + 1, current_power + 2
            # So, we look for the last power that is not within the range [current_power - 2, current_power + 2]
            j = i - 1
            while j >= 0 and unique_powers[j] >= current_power - 2:
                j -= 1
            dp[i] = max(dp[i], dp[j + 1] + current_power * power_count[current_power])
        
        return dp[-1]

def maximumTotalDamage(power: List[int]) -> int:
    return Solution().maximumTotalDamage(power)