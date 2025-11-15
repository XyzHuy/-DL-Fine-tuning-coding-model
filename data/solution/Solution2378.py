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
    def maxScore(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Build the adjacency list
        tree = defaultdict(list)
        for i in range(1, len(edges)):
            parent, weight = edges[i]
            tree[parent].append((i, weight))
        
        @lru_cache(None)
        def dp(node, include_parent_edge):
            if not tree[node]:
                return 0 if include_parent_edge else 0
            
            # Option 1: Do not include the edge from parent to node
            sum_excluding_edge = sum(dp(child, False) for child, weight in tree[node])
            
            # Option 2: Include the edge from parent to node
            sum_including_edge = 0
            for child, weight in tree[node]:
                sum_including_edge = max(sum_including_edge,
                                         sum_excluding_edge - dp(child, False) + weight + dp(child, True))
            
            if include_parent_edge:
                return sum_excluding_edge
            else:
                return max(sum_excluding_edge, sum_including_edge)
        
        # Start from the root node with the option of not including the parent edge
        return dp(0, False)

def maxScore(edges: List[List[int]]) -> int:
    return Solution().maxScore(edges)