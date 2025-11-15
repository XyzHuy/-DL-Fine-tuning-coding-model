import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        
        # Step 1: Create adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # Step 2: Function to perform BFS and find the size of a connected component
        def bfs(start):
            queue = deque([start])
            visited.add(start)
            size = 0
            while queue:
                node = queue.popleft()
                size += 1
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            return size
        
        # Step 3: Find all connected components and their sizes
        visited = set()
        component_sizes = []
        
        for i in range(n):
            if i not in visited:
                component_size = bfs(i)
                component_sizes.append(component_size)
        
        # Step 4: Calculate the number of unreachable pairs
        total_unreachable_pairs = 0
        total_nodes = n
        
        for size in component_sizes:
            total_unreachable_pairs += size * (total_nodes - size)
        
        # Since each pair is counted twice, we divide by 2
        return total_unreachable_pairs // 2

# Example usage:
# sol = Solution()
# print(sol.countPairs(3, [[0,1],[0,2],[1,2]]))  # Output: 0
# print(sol.countPairs(7, [[0,2],[0,5],[2,4],[1,6],[5,4]]))  # Output: 14

def countPairs(n: int, edges: List[List[int]]) -> int:
    return Solution().countPairs(n, edges)