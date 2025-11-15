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
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Build the graph using adjacency list
        subordinates = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)
        
        # Depth-First Search to calculate the time needed to inform all employees
        def dfs(employee_id: int) -> int:
            if not subordinates[employee_id]:
                return 0
            max_time = 0
            for subordinate in subordinates[employee_id]:
                max_time = max(max_time, dfs(subordinate))
            return max_time + informTime[employee_id]
        
        # Start DFS from the head of the company
        return dfs(headID)

def numOfMinutes(n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    return Solution().numOfMinutes(n, headID, manager, informTime)