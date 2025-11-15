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
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        def dfs(node, parent, target):
            total = nums[node]
            for neighbor in g[node]:
                if neighbor == parent:
                    continue
                subtree_sum, is_valid = dfs(neighbor, node, target)
                if not is_valid:
                    return (0, False)
                total += subtree_sum
            if total > target:
                return (0, False)
            if total == target:
                return (0, True)
            return (total, True)
        
        n = len(nums)
        total_sum = sum(nums)
        
        # Create adjacency list for the tree
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        # Check all divisors of total_sum as potential component values
        max_deletions = 0
        for components in range(2, n + 1):
            if total_sum % components == 0:
                target = total_sum // components
                _, is_possible = dfs(0, -1, target)
                if is_possible:
                    max_deletions = components - 1
        
        return max_deletions

def componentValue(nums: List[int], edges: List[List[int]]) -> int:
    return Solution().componentValue(nums, edges)