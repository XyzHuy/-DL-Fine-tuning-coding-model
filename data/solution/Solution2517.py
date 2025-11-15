import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # Sort the prices to facilitate the binary search
        price.sort()
        
        # Helper function to check if we can pick k candies with at least 'min_tastiness' difference
        def can_pick_k_candies(min_tastiness: int) -> bool:
            count = 0
            last_picked = -float('inf')
            for p in price:
                if p - last_picked >= min_tastiness:
                    count += 1
                    last_picked = p
                if count >= k:
                    return True
            return False
        
        # Binary search for the maximum tastiness
        left, right = 0, price[-1] - price[0]
        best_tastiness = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_pick_k_candies(mid):
                best_tastiness = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best_tastiness

def maximumTastiness(price: List[int], k: int) -> int:
    return Solution().maximumTastiness(price, k)