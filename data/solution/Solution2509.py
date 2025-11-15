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
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def find_lca(a, b):
            steps = 0
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                steps += 1
            return steps
        
        result = []
        for a, b in queries:
            cycle_length = find_lca(a, b) + 1
            result.append(cycle_length)
        
        return result

def cycleLengthQueries(n: int, queries: List[List[int]]) -> List[int]:
    return Solution().cycleLengthQueries(n, queries)