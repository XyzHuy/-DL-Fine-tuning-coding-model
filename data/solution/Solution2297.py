import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def minCost(self, nums: List[int], costs: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        # Arrays to store the next greater or equal and next smaller elements
        next_greater_equal = [-1] * n
        next_smaller = [-1] * n
        
        # Monotonic stacks to find the next greater or equal and next smaller elements
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                next_greater_equal[stack.pop()] = i
            stack.append(i)
        
        stack.clear()
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                next_smaller[stack.pop()] = i
            stack.append(i)
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, 0)]  # (current_cost, current_index)
        visited = [False] * n
        min_cost = [float('inf')] * n
        min_cost[0] = 0
        
        while pq:
            current_cost, current_index = heapq.heappop(pq)
            
            if visited[current_index]:
                continue
            
            visited[current_index] = True
            
            # Explore the next greater or equal index
            if next_greater_equal[current_index] != -1:
                neighbor = next_greater_equal[current_index]
                new_cost = current_cost + costs[neighbor]
                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
            
            # Explore the next smaller index
            if next_smaller[current_index] != -1:
                neighbor = next_smaller[current_index]
                new_cost = current_cost + costs[neighbor]
                if new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))
        
        return min_cost[n - 1]

def minCost(nums: List[int], costs: List[int]) -> int:
    return Solution().minCost(nums, costs)