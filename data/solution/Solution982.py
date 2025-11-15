import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from typing import List

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        # Dictionary to store the frequency of each pairwise AND result
        pair_and_count = defaultdict(int)
        
        # Precompute the AND results for all pairs
        for num1 in nums:
            for num2 in nums:
                pair_and_count[num1 & num2] += 1
        
        # Count the number of valid triplets
        triplet_count = 0
        for num in nums:
            for pair_and, count in pair_and_count.items():
                if num & pair_and == 0:
                    triplet_count += count
        
        return triplet_count

# Example usage:
# sol = Solution()
# print(sol.countTriplets([2, 1, 3]))  # Output: 12
# print(sol.countTriplets([0, 0, 0]))  # Output: 27

def countTriplets(nums: List[int]) -> int:
    return Solution().countTriplets(nums)