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
from math import comb

MOD = 10**9 + 7

class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        n = len(prevRoom)
        # Build the graph
        graph = [[] for _ in range(n)]
        for i in range(1, n):
            graph[prevRoom[i]].append(i)
        
        # DFS function to calculate the number of ways to build the subtree rooted at node
        def dfs(node):
            if not graph[node]:
                return 1, 1  # (number of ways, total number of rooms in the subtree)
            total_ways = 1
            total_rooms = 0
            for child in graph[node]:
                child_ways, child_rooms = dfs(child)
                total_ways = (total_ways * child_ways * comb(total_rooms + child_rooms, child_rooms)) % MOD
                total_rooms += child_rooms
            return total_ways, total_rooms + 1
        
        return dfs(0)[0]

def waysToBuildRooms(prevRoom: List[int]) -> int:
    return Solution().waysToBuildRooms(prevRoom)