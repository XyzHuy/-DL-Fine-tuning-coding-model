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
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        # Step 1: Build the adjacency list for the tree
        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Precompute coprime relationships for numbers from 1 to 50
        coprimes = defaultdict(set)
        for x in range(1, 51):
            for y in range(1, 51):
                if gcd(x, y) == 1:
                    coprimes[x].add(y)
        
        # Step 3: Initialize the result list and ancestor stack
        result = [-1] * n
        ancestor_stack = defaultdict(list)
        
        # Step 4: Define the DFS function
        def dfs(node, parent, depth):
            # Find the closest coprime ancestor
            max_depth = -1
            for value in coprimes[nums[node]]:
                if ancestor_stack[value]:
                    last_depth, last_ancestor = ancestor_stack[value][-1]
                    if last_depth > max_depth:
                        max_depth = last_depth
                        result[node] = last_ancestor
            
            # Add the current node to the ancestor stack
            ancestor_stack[nums[node]].append((depth, node))
            
            # Recursively visit the children
            for child in graph[node]:
                if child != parent:
                    dfs(child, node, depth + 1)
            
            # Backtrack: remove the current node from the ancestor stack
            ancestor_stack[nums[node]].pop()
        
        # Step 5: Start DFS from the root (node 0)
        dfs(0, -1, 0)
        
        return result

# Helper function to compute the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def getCoprimes(nums: List[int], edges: List[List[int]]) -> List[int]:
    return Solution().getCoprimes(nums, edges)