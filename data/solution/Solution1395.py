import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        count = 0
        
        # Iterate over each soldier as the middle soldier (j)
        for j in range(1, n - 1):
            # Count soldiers with lower rating than rating[j] to the left (i < j)
            left_lower = 0
            # Count soldiers with higher rating than rating[j] to the left (i < j)
            left_higher = 0
            # Count soldiers with lower rating than rating[j] to the right (j < k)
            right_lower = 0
            # Count soldiers with higher rating than rating[j] to the right (j < k)
            right_higher = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_lower += 1
                else:
                    left_higher += 1
            
            for k in range(j + 1, n):
                if rating[j] < rating[k]:
                    right_higher += 1
                else:
                    right_lower += 1
            
            # Valid increasing team: left_lower soldiers to choose from for i, right_higher soldiers to choose from for k
            # Valid decreasing team: left_higher soldiers to choose from for i, right_lower soldiers to choose from for k
            count += (left_lower * right_higher) + (left_higher * right_lower)
        
        return count

def numTeams(rating: List[int]) -> int:
    return Solution().numTeams(rating)