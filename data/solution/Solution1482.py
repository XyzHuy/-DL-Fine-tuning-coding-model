import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        
        def canMakeBouquets(day):
            flowers = 0
            bouquets = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                else:
                    bouquets += flowers // k
                    flowers = 0
            bouquets += flowers // k
            return bouquets >= m
        
        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            if canMakeBouquets(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

def minDays(bloomDay: List[int], m: int, k: int) -> int:
    return Solution().minDays(bloomDay, m, k)