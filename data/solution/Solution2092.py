import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # Sort meetings by time
        meetings.sort(key=lambda x: x[2])
        
        # Initialize the set of people who know the secret
        known_people = {0, firstPerson}
        
        # Process meetings in chronological order
        i = 0
        while i < len(meetings):
            # Collect all meetings happening at the current time
            current_time = meetings[i][2]
            graph = defaultdict(list)
            while i < len(meetings) and meetings[i][2] == current_time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                i += 1
            
            # Perform BFS to find all connected components that include a person who knows the secret
            queue = deque([person for person in graph.keys() if person in known_people])
            visited = set(queue)
            
            while queue:
                person = queue.popleft()
                for neighbor in graph[person]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            # Update the set of people who know the secret
            known_people.update(visited)
        
        return list(known_people)

def findAllPeople(n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    return Solution().findAllPeople(n, meetings, firstPerson)