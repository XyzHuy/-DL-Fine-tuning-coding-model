import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
from bisect import bisect_right

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by time
        logs.sort(key=lambda log: log[1])
        
        # Create a dictionary to store the list of times each server received a request
        server_times = defaultdict(list)
        for server_id, time in logs:
            server_times[server_id].append(time)
        
        # Sort queries and keep track of their original indices
        sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
        
        result = [0] * len(queries)
        current_servers = set()
        log_index = 0
        
        for original_index, query_time in sorted_queries:
            start_time = query_time - x
            
            # Add servers that received requests in the interval [start_time, query_time]
            for server_id in range(1, n + 1):
                times = server_times[server_id]
                # Find the rightmost log time that is <= query_time
                end_index = bisect_right(times, query_time)
                # Find the rightmost log time that is < start_time
                start_index = bisect_right(times, start_time - 1)
                if start_index < end_index:
                    current_servers.add(server_id)
            
            # Remove servers that did not receive requests in the interval [start_time, query_time]
            for server_id in list(current_servers):
                times = server_times[server_id]
                end_index = bisect_right(times, query_time)
                start_index = bisect_right(times, start_time - 1)
                if start_index >= end_index:
                    current_servers.remove(server_id)
            
            # The number of servers that did not receive any requests in the interval
            result[original_index] = n - len(current_servers)
        
        return result

def countServers(n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
    return Solution().countServers(n, logs, x, queries)