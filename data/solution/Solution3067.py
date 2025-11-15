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
from typing import List
from collections import defaultdict

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        # Build the graph
        graph = defaultdict(list)
        for a, b, weight in edges:
            graph[a].append((b, weight))
            graph[b].append((a, weight))
        
        def dfs(node, parent, distance):
            count = 0
            if distance % signalSpeed == 0:
                count += 1
            for neighbor, weight in graph[node]:
                if neighbor != parent:
                    count += dfs(neighbor, node, distance + weight)
            return count
        
        n = len(graph)
        result = [0] * n
        
        for c in range(n):
            groups = []
            for neighbor, weight in graph[c]:
                count = dfs(neighbor, c, weight)
                groups.append(count)
            
            # Calculate the number of connectable pairs for server c
            total_pairs = 0
            for i in range(len(groups)):
                for j in range(i + 1, len(groups)):
                    total_pairs += groups[i] * groups[j]
            result[c] = total_pairs
        
        return result

def countPairsOfConnectableServers(edges: List[List[int]], signalSpeed: int) -> List[int]:
    return Solution().countPairsOfConnectableServers(edges, signalSpeed)