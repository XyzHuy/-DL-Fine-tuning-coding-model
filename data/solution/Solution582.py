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
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # Create a dictionary to map each parent process to its children
        process_tree = defaultdict(list)
        for child, parent in zip(pid, ppid):
            process_tree[parent].append(child)
        
        # Function to perform a depth-first search (DFS) to find all processes to be killed
        def dfs(process_id):
            # Start with the process to be killed
            processes_to_kill = [process_id]
            # Explore all children of the current process
            for child in process_tree[process_id]:
                processes_to_kill.extend(dfs(child))
            return processes_to_kill
        
        # Return the list of processes that will be killed
        return dfs(kill)

def killProcess(pid: List[int], ppid: List[int], kill: int) -> List[int]:
    return Solution().killProcess(pid, ppid, kill)