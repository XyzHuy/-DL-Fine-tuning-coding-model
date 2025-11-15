import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        if candidates * 2 >= n:
            # If the number of candidates from both ends is greater than or equal to the total number of workers,
            # we can just sort the entire list and take the first k elements.
            return sum(sorted(costs)[:k])
        
        # Min-heaps for the first and last candidates
        left_heap = [(costs[i], i) for i in range(candidates)]
        right_heap = [(costs[i], i) for i in range(n - candidates, n)]
        
        heapq.heapify(left_heap)
        heapq.heapify(right_heap)
        
        left_index = candidates
        right_index = n - candidates - 1
        total_cost = 0
        
        for _ in range(k):
            if not left_heap or (right_heap and right_heap[0] < left_heap[0]):
                # Hire from the right heap
                cost, index = heapq.heappop(right_heap)
                total_cost += cost
                if left_index <= right_index:
                    heapq.heappush(right_heap, (costs[right_index], right_index))
                    right_index -= 1
            else:
                # Hire from the left heap
                cost, index = heapq.heappop(left_heap)
                total_cost += cost
                if left_index <= right_index:
                    heapq.heappush(left_heap, (costs[left_index], left_index))
                    left_index += 1
        
        return total_cost

def totalCost(costs: List[int], k: int, candidates: int) -> int:
    return Solution().totalCost(costs, k, candidates)