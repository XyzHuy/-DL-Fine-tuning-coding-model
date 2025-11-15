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
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Store guesses in a set for O(1) lookup
        guess_set = set((u, v) for u, v in guesses)
        
        # DFS to count correct guesses assuming root is 0
        def dfs(node, parent):
            count = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if (node, neighbor) in guess_set:
                    count += 1
                count += dfs(neighbor, node)
            return count
        
        # Initial count of correct guesses with root 0
        correct_guesses_from_0 = dfs(0, -1)
        
        # DFS to re-root the tree and count correct guesses
        def re_root_dfs(node, parent, current_count):
            nonlocal result
            if current_count >= k:
                result += 1
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                
                # Try making neighbor the new root
                if (node, neighbor) in guess_set:
                    new_count = current_count - 1
                else:
                    new_count = current_count
                
                if (neighbor, node) in guess_set:
                    new_count += 1
                
                re_root_dfs(neighbor, node, new_count)
        
        result = 0
        re_root_dfs(0, -1, correct_guesses_from_0)
        
        return result

def rootCount(edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
    return Solution().rootCount(edges, guesses, k)