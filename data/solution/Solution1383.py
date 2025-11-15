import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # Combine efficiency and speed into a single list of tuples
        engineers = list(zip(efficiency, speed))
        
        # Sort engineers by efficiency in descending order
        engineers.sort(reverse=True)
        
        # Min-heap to keep track of the k smallest speeds
        speed_heap = []
        total_speed = 0
        max_performance = 0
        MOD = 10**9 + 7
        
        for eff, spd in engineers:
            # Add the current engineer's speed to the heap
            heapq.heappush(speed_heap, spd)
            total_speed += spd
            
            # If we have more than k engineers, remove the smallest speed
            if len(speed_heap) > k:
                total_speed -= heapq.heappop(speed_heap)
            
            # Calculate the performance with the current engineer's efficiency
            current_performance = total_speed * eff
            max_performance = max(max_performance, current_performance)
        
        return max_performance % MOD

def maxPerformance(n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    return Solution().maxPerformance(n, speed, efficiency, k)