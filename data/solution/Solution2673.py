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

class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def dfs(node: int) -> (int, int):
            if node > n:
                return 0, 0
            
            left_total, left_increments = dfs(2 * node)
            right_total, right_increments = dfs(2 * node + 1)
            
            current_total = cost[node - 1] + max(left_total, right_total)
            current_increments = left_increments + right_increments + abs(left_total - right_total)
            
            return current_total, current_increments
        
        _, total_increments = dfs(1)
        return total_increments

def minIncrements(n: int, cost: List[int]) -> int:
    return Solution().minIncrements(n, cost)