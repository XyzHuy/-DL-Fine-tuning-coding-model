import heapq
import itertools
from sortedcontainers import SortedList
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
import bisect

class Solution:
    def maxDepthBST(self, order: List[int]) -> int:
        if not order:
            return 0
        
        sorted_list = []
        depth = {}
        max_depth = 0
        
        for x in order:
            idx = bisect.bisect_left(sorted_list, x)
            predecessor = sorted_list[idx-1] if idx > 0 else None
            successor = sorted_list[idx] if idx < len(sorted_list) else None
            
            current_depth = 1
            if predecessor is not None:
                current_depth = max(current_depth, depth[predecessor] + 1)
            if successor is not None:
                current_depth = max(current_depth, depth[successor] + 1)
            
            depth[x] = current_depth
            if current_depth > max_depth:
                max_depth = current_depth
            
            bisect.insort(sorted_list, x)
        
        return max_depth

def maxDepthBST(order: List[int]) -> int:
    return Solution().maxDepthBST(order)