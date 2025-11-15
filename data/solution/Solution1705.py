import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        eaten = 0
        min_heap = []  # (rot_day, count)

        for i in range(len(apples)):
            # Add new apples to the heap with their rot day
            if apples[i] > 0:
                heapq.heappush(min_heap, (i + days[i], apples[i]))
            
            # Remove rotten apples from the heap
            while min_heap and (min_heap[0][0] <= i or min_heap[0][1] == 0):
                heapq.heappop(min_heap)
            
            # Eat an apple from the batch that will rot the earliest
            if min_heap:
                rot_day, count = heapq.heappop(min_heap)
                eaten += 1
                if count > 1:
                    heapq.heappush(min_heap, (rot_day, count - 1))
        
        # Continue eating apples after the last day if there are any left
        day = len(apples)
        while min_heap:
            while min_heap and (min_heap[0][0] <= day or min_heap[0][1] == 0):
                heapq.heappop(min_heap)
            if min_heap:
                rot_day, count = heapq.heappop(min_heap)
                days_left = min(rot_day - day, count)
                eaten += days_left
                day += days_left
        
        return eaten

def eatenApples(apples: List[int], days: List[int]) -> int:
    return Solution().eatenApples(apples, days)