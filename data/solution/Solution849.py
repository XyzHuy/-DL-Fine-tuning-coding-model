import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_distance = 0
        start = 0
        n = len(seats)
        
        # Find the first occupied seat
        while seats[start] == 0:
            start += 1
        
        # Calculate the distance from the start to the first occupied seat
        max_distance = start
        
        # Find the maximum distance between two occupied seats
        last = start
        for i in range(start + 1, n):
            if seats[i] == 1:
                # Calculate the distance between last occupied seat and current one
                distance = (i - last) // 2
                max_distance = max(max_distance, distance)
                last = i
        
        # Calculate the distance from the last occupied seat to the end
        max_distance = max(max_distance, n - last - 1)
        
        return max_distance

def maxDistToClosest(seats: List[int]) -> int:
    return Solution().maxDistToClosest(seats)