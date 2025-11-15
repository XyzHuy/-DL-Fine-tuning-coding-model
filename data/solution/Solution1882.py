import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Initialize the available servers heap with (weight, index) tuples
        available_servers = [(weight, index) for index, weight in enumerate(servers)]
        heapq.heapify(available_servers)
        
        # Busy servers heap will store (end_time, weight, index) tuples
        busy_servers = []
        
        # Result list to store the server index for each task
        result = []
        
        # Current time and task index
        current_time = 0
        task_index = 0
        
        while task_index < len(tasks):
            # Move servers that have completed their tasks from busy to available
            while busy_servers and busy_servers[0][0] <= current_time:
                _, weight, index = heapq.heappop(busy_servers)
                heapq.heappush(available_servers, (weight, index))
            
            # Assign tasks to available servers
            while task_index <= current_time and task_index < len(tasks) and available_servers:
                weight, index = heapq.heappop(available_servers)
                result.append(index)
                heapq.heappush(busy_servers, (current_time + tasks[task_index], weight, index))
                task_index += 1
            
            # If there are no available servers, fast forward to the next time a server becomes available
            if not available_servers:
                current_time = busy_servers[0][0]
            else:
                current_time += 1
        
        return result

def assignTasks(servers: List[int], tasks: List[int]) -> List[int]:
    return Solution().assignTasks(servers, tasks)