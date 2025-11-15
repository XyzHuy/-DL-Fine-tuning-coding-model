import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dp(i, amount, coupons):
            if i == len(price):
                return 0
            
            # Option 1: Do not buy the current fruit
            max_tastiness = dp(i + 1, amount, coupons)
            
            # Option 2: Buy the current fruit without a coupon
            if amount >= price[i]:
                max_tastiness = max(max_tastiness, tastiness[i] + dp(i + 1, amount - price[i], coupons))
            
            # Option 3: Buy the current fruit with a coupon
            if coupons > 0 and amount >= price[i] // 2:
                max_tastiness = max(max_tastiness, tastiness[i] + dp(i + 1, amount - price[i] // 2, coupons - 1))
            
            return max_tastiness
        
        return dp(0, maxAmount, maxCoupons)

def maxTastiness(price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
    return Solution().maxTastiness(price, tastiness, maxAmount, maxCoupons)