import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # Calculate the prefix sum of candiesCount
        prefix_sum = [0] * (len(candiesCount) + 1)
        for i in range(len(candiesCount)):
            prefix_sum[i + 1] = prefix_sum[i] + candiesCount[i]
        
        answer = []
        for favoriteType, favoriteDay, dailyCap in queries:
            # Calculate the minimum and maximum day we can start eating the favorite type
            min_day = prefix_sum[favoriteType] // dailyCap
            max_day = prefix_sum[favoriteType + 1]
            
            # Check if we can eat the favorite type on the favorite day
            if min_day <= favoriteDay < max_day:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer

def canEat(candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
    return Solution().canEat(candiesCount, queries)