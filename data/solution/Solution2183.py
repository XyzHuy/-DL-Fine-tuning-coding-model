import random
import functools
import collections
import string
import math
import datetime


from typing import List
from math import gcd
from collections import Counter

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        gcd_counts = Counter()
        
        # Count the frequency of each gcd with k
        for num in nums:
            gcd_counts[gcd(num, k)] += 1
        
        result = 0
        
        # Iterate over all unique gcds
        for g1 in gcd_counts:
            for g2 in gcd_counts:
                if g1 <= g2 and (g1 * g2) % k == 0:
                    if g1 == g2:
                        # If g1 == g2, we need to choose 2 out of gcd_counts[g1] numbers
                        result += gcd_counts[g1] * (gcd_counts[g1] - 1) // 2
                    else:
                        # If g1 < g2, we can pair each g1 with each g2
                        result += gcd_counts[g1] * gcd_counts[g2]
        
        return result

# Example usage:
# sol = Solution()
# print(sol.countPairs([1,2,3,4,5], 2))  # Output: 7
# print(sol.countPairs([1,2,3,4], 5))    # Output: 0

def countPairs(nums: List[int], k: int) -> int:
    return Solution().countPairs(nums, k)