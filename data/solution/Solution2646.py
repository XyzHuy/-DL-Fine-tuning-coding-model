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
from collections import defaultdict, Counter
from typing import List

class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # Step 1: Build the adjacency list for the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Function to find the path from start to end using DFS
        def find_path(start, end, parent):
            if start == end:
                return [start]
            for neighbor in graph[start]:
                if neighbor != parent:
                    path = find_path(neighbor, end, start)
                    if path:
                        return [start] + path
            return None
        
        # Step 3: Count the frequency of each node being visited across all trips
        node_count = Counter()
        for start, end in trips:
            path = find_path(start, end, -1)
            for node in path:
                node_count[node] += 1
        
        # Step 4: Calculate the total cost without any price reductions
        total_cost = sum(node_count[node] * price[node] for node in node_count)
        
        # Step 5: Dynamic Programming on Trees
        # dp[node][0]: cost if we do not halve the price of node
        # dp[node][1]: cost if we halve the price of node
        dp = [[0, 0] for _ in range(n)]
        
        def dfs(node, parent):
            dp[node][0] = node_count[node] * price[node]
            dp[node][1] = dp[node][0] // 2
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    dp[node][0] += min(dp[neighbor][0], dp[neighbor][1])
                    dp[node][1] += dp[neighbor][0]
        
        # Start DFS from any node, as it is a tree
        dfs(0, -1)
        
        # Step 6: The result is the minimum of the two states for the root node
        return min(dp[0][0], dp[0][1])

def minimumTotalPrice(n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
    return Solution().minimumTotalPrice(n, edges, price, trips)