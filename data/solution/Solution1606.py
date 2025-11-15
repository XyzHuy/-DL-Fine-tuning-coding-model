import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # This will keep track of the number of requests handled by each server
        request_count = [0] * k
        # This is a min-heap to keep track of busy servers (end_time, server_id)
        busy_servers = []
        # This is a sorted list to keep track of available servers
        available_servers = list(range(k))
        
        for i, (start_time, task_load) in enumerate(zip(arrival, load)):
            # Index of the preferred server
            preferred_server = i % k
            
            # Free up servers that have completed their tasks by the current start_time
            while busy_servers and busy_servers[0][0] <= start_time:
                _, freed_server = heapq.heappop(busy_servers)
                # Insert the freed server into the available servers in a circular fashion
                heapq.heappush(available_servers, i + (freed_server - i) % k)
            
            # Check if there is any available server
            if available_servers:
                # Assign the task to the next available server
                assigned_server = heapq.heappop(available_servers) % k
                # Increment the request count for the assigned server
                request_count[assigned_server] += 1
                # Push the server into the busy servers heap with its end time
                heapq.heappush(busy_servers, (start_time + task_load, assigned_server))
        
        # Find the maximum number of requests handled by any server
        max_requests = max(request_count)
        # Collect all servers that handled the maximum number of requests
        busiest_servers = [i for i, count in enumerate(request_count) if count == max_requests]
        
        return busiest_servers

def busiestServers(k: int, arrival: List[int], load: List[int]) -> List[int]:
    return Solution().busiestServers(k, arrival, load)