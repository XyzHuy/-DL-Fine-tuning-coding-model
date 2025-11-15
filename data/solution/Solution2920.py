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
from functools import lru_cache

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        from collections import defaultdict
        
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Memoization decorator
        @lru_cache(None)
        def dfs(node, parent, halves):
            # If we've halved the coins 14 times, further halving won't change the result
            if halves >= 14:
                return 0
            
            # Calculate the current coins value
            current_coins = coins[node] >> halves
            
            # Strategy 1: Collect all coins and get current_coins - k points
            points1 = current_coins - k
            
            # Strategy 2: Collect all coins and get current_coins // 2 points
            points2 = current_coins >> 1
            
            # Recursively calculate points for children
            for child in graph[node]:
                if child != parent:
                    points1 += dfs(child, node, halves)
                    points2 += dfs(child, node, halves + 1)
            
            # Return the maximum points from the two strategies
            return max(points1, points2)
        
        # Start DFS from the root node (0) with 0 halves
        return dfs(0, -1, 0)

def maximumPoints(edges: List[List[int]], coins: List[int], k: int) -> int:
    return Solution().maximumPoints(edges, coins, k)