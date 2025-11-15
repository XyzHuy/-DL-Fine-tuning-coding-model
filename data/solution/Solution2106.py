import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        max_fruits = 0
        total_fruits = 0
        left = 0
        
        for right in range(n):
            total_fruits += fruits[right][1]
            
            while left <= right and (min(abs(startPos - fruits[left][0]), abs(startPos - fruits[right][0])) + 
                                    fruits[right][0] - fruits[left][0] > k):
                total_fruits -= fruits[left][1]
                left += 1
            
            max_fruits = max(max_fruits, total_fruits)
        
        return max_fruits

def maxTotalFruits(fruits: List[List[int]], startPos: int, k: int) -> int:
    return Solution().maxTotalFruits(fruits, startPos, k)