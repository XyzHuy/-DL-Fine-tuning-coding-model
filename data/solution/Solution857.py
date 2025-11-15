import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # Calculate the ratio of wage to quality for each worker
        unit_price = sorted([(wage[i] / quality[i], quality[i]) for i in range(len(quality))])
        
        # Max heap to store the negative quality values (to simulate a min heap with max heap functionality)
        max_heap = []
        total_quality = 0
        min_cost = float('inf')
        
        # Iterate over the sorted unit prices
        for price, qual in unit_price:
            # Add the current worker's quality to the heap and total quality
            heapq.heappush(max_heap, -qual)
            total_quality += qual
            
            # If we have more than k workers, remove the worker with the highest quality (most expensive)
            if len(max_heap) > k:
                total_quality += heapq.heappop(max_heap)
            
            # If we have exactly k workers, calculate the cost
            if len(max_heap) == k:
                min_cost = min(min_cost, price * total_quality)
        
        return min_cost

def mincostToHireWorkers(quality: List[int], wage: List[int], k: int) -> float:
    return Solution().mincostToHireWorkers(quality, wage, k)