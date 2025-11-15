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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque
from typing import Optional

class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        # Convert the tree to an undirected graph
        graph = defaultdict(list)
        
        def build_graph(node, parent=None):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                build_graph(node.left, node)
                build_graph(node.right, node)
        
        build_graph(root)
        
        # BFS to find the nearest leaf from node k
        queue = deque([k])
        visited = set()
        
        while queue:
            current = queue.popleft()
            visited.add(current)
            
            # If the current node is a leaf, return it
            if len(graph[current]) <= 1 and current != root.val:
                return current
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        # In case the root itself is the only node or the only leaf
        return root.val

def findClosestLeaf(root: Optional[TreeNode], k: int) -> int:
    return Solution().findClosestLeaf(root, k)