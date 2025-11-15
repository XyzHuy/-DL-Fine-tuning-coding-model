import random
import functools
import collections
import string
import math
import datetime


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_node(values: list):
    if not values:
        return None
    root = TreeNode(values[0])
    i = 1
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def is_same_tree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
from collections import deque, defaultdict
from typing import List

class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        graph = defaultdict(list)
        
        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def bfs(start):
            # Initialize the queue with the starting node marked at time 0
            queue = deque([(start, 0)])
            marked = [False] * n
            marked[start] = True
            max_time = 0
            
            while queue:
                node, time = queue.popleft()
                max_time = max(max_time, time)
                
                for neighbor in graph[node]:
                    if not marked[neighbor]:
                        marked[neighbor] = True
                        if neighbor % 2 == 1:
                            queue.append((neighbor, time + 1))
                        else:
                            queue.append((neighbor, time + 2))
            
            return max_time
        
        # Calculate the time taken for each node to mark all nodes
        times = [0] * n
        for i in range(n):
            times[i] = bfs(i)
        
        return times

def timeTaken(edges: List[List[int]]) -> List[int]:
    return Solution().timeTaken(edges)