import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # Build the graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        
        for prevCourse, nextCourse in relations:
            graph[prevCourse].append(nextCourse)
            in_degree[nextCourse] += 1
        
        # Initialize the queue with courses having no prerequisites
        queue = deque()
        for course in range(1, n + 1):
            if in_degree[course] == 0:
                queue.append(course)
        
        # Process the courses level by level (semester by semester)
        semesters = 0
        taken_courses = 0
        
        while queue:
            semesters += 1
            for _ in range(len(queue)):
                current_course = queue.popleft()
                taken_courses += 1
                for next_course in graph[current_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
        
        # If all courses are taken, return the number of semesters, otherwise -1
        return semesters if taken_courses == n else -1

def minimumSemesters(n: int, relations: List[List[int]]) -> int:
    return Solution().minimumSemesters(n, relations)