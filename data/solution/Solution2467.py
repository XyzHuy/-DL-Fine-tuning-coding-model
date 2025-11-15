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
from collections import defaultdict, deque

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Find the path from bob to root (node 0) using BFS
        parent = {0: None}
        queue = deque([0])
        found = False
        
        while queue:
            node = queue.popleft()
            if node == bob:
                found = True
                break
            for neighbor in graph[node]:
                if neighbor not in parent:
                    parent[neighbor] = node
                    queue.append(neighbor)
        
        if not found:
            return amount[0]
        
        # Trace back the path from bob to root
        bob_path = {}
        steps = 0
        while bob is not None:
            bob_path[bob] = steps
            steps += 1
            bob = parent[bob]
        
        # Perform a DFS to find the maximum profit for Alice
        def dfs(node, step, profit, visited):
            visited.add(node)
            if node not in bob_path or step < bob_path[node]:
                profit += amount[node]
            elif step == bob_path[node]:
                profit += amount[node] // 2
            
            max_profit = float('-inf')
            children = [neighbor for neighbor in graph[node] if neighbor not in visited]
            if not children:  # Leaf node
                return profit
            
            for neighbor in children:
                max_profit = max(max_profit, dfs(neighbor, step + 1, profit, visited))
            
            visited.remove(node)
            return max_profit
        
        return dfs(0, 0, 0, set())

def mostProfitablePath(edges: List[List[int]], bob: int, amount: List[int]) -> int:
    return Solution().mostProfitablePath(edges, bob, amount)