import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict, deque
        
        # Create a graph
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Build the graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # Add all courses with no prerequisites to the queue
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        
        # Process the queue
        while queue:
            course = queue.popleft()
            numCourses -= 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        return numCourses == 0

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    return Solution().canFinish(numCourses, prerequisites)