import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create a graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph and fill in-degree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Initialize the queue with all courses having 0 in-degree
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        result = []
        
        # Process nodes in the queue
        while queue:
            course = queue.popleft()
            result.append(course)
            
            # Decrease the in-degree of adjacent courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If in-degree becomes 0, add to the queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # If we have processed all courses, return the result
        return result if len(result) == numCourses else []

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    return Solution().findOrder(numCourses, prerequisites)