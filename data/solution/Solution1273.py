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
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        # Build the tree as an adjacency list
        tree = defaultdict(list)
        for i in range(nodes):
            if parent[i] != -1:
                tree[parent[i]].append(i)
        
        # Function to perform DFS and calculate subtree sums
        def dfs(node):
            subtree_sum = value[node]
            count = 1  # Count this node itself
            
            for child in tree[node]:
                child_sum, child_count = dfs(child)
                subtree_sum += child_sum
                count += child_count
            
            # If the subtree sum is zero, we delete this subtree
            if subtree_sum == 0:
                count = 0
            
            return subtree_sum, count
        
        # Start DFS from the root node (0)
        _, remaining_nodes = dfs(0)
        return remaining_nodes

def deleteTreeNodes(nodes: int, parent: List[int], value: List[int]) -> int:
    return Solution().deleteTreeNodes(nodes, parent, value)