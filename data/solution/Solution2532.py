import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        # Define the priority queues for workers on the left and right side
        left_side = []
        right_side = []
        # Define the priority queues for workers who have just crossed the bridge and are busy with tasks
        left_tasks = []
        right_tasks = []
        
        # Organize workers based on their efficiency
        for i in range(k):
            efficiency = -(time[i][0] + time[i][2])  # Negative for max-heap behavior
            heapq.heappush(left_side, (efficiency, -i))
        
        current_time = 0
        
        while n > 0 or right_side or right_tasks:
            # Move workers from right_tasks to right_side if their tasks are complete
            while right_tasks and right_tasks[0][0] <= current_time:
                _, efficiency, worker_idx = heapq.heappop(right_tasks)
                heapq.heappush(right_side, (efficiency, worker_idx))
            
            # Move workers from left_tasks to left_side if their tasks are complete
            while left_tasks and left_tasks[0][0] <= current_time:
                _, efficiency, worker_idx = heapq.heappop(left_tasks)
                heapq.heappush(left_side, (efficiency, worker_idx))
            
            # If there are workers on the right side ready to cross, let the least efficient cross
            if right_side:
                efficiency, worker_idx = heapq.heappop(right_side)
                current_time += time[-worker_idx][2]  # They cross to the left
                heapq.heappush(left_tasks, (current_time + time[-worker_idx][3], efficiency, worker_idx))
            # Otherwise, if there are workers on the left side and we still need to pick more boxes, let the least efficient cross
            elif n > 0 and left_side:
                efficiency, worker_idx = heapq.heappop(left_side)
                current_time += time[-worker_idx][0]  # They cross to the right
                heapq.heappush(right_tasks, (current_time + time[-worker_idx][1], efficiency, worker_idx))
                n -= 1
            # If no workers are ready to cross, advance the time to the next worker completing a task
            else:
                next_time = float('inf')
                if right_tasks:
                    next_time = min(next_time, right_tasks[0][0])
                if left_tasks:
                    next_time = min(next_time, left_tasks[0][0])
                if next_time < float('inf'):
                    current_time = next_time
        
        return current_time

def findCrossingTime(n: int, k: int, time: List[List[int]]) -> int:
    return Solution().findCrossingTime(n, k, time)