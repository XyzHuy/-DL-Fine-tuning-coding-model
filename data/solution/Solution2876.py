import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        visited = [0] * n  # 0 means unvisited, 1 means visiting, 2 means visited
        answer = [0] * n
        node_to_cycle = [-1] * n  # To store the index of the cycle each node belongs to
        cycle_lengths = {}  # To store the length of each cycle
        
        def dfs(node, cycle_index):
            if visited[node] == 2:
                return answer[node]
            if visited[node] == 1:
                # We've found a cycle
                cycle_node = node
                cycle_length = 0
                while True:
                    cycle_length += 1
                    node_to_cycle[cycle_node] = cycle_index
                    if edges[cycle_node] == node:
                        break
                    cycle_node = edges[cycle_node]
                cycle_lengths[cycle_index] = cycle_length
                return cycle_length
            visited[node] = 1
            next_node = edges[node]
            path_length = dfs(next_node, cycle_index) + 1
            visited[node] = 2
            if node_to_cycle[node] != -1:
                # This node is part of a cycle
                cycle_index = node_to_cycle[node]
                answer[node] = cycle_lengths[cycle_index]
            else:
                answer[node] = path_length
            return answer[node]
        
        cycle_index = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, cycle_index)
                cycle_index += 1
        
        return answer

def countVisitedNodes(edges: List[int]) -> List[int]:
    return Solution().countVisitedNodes(edges)