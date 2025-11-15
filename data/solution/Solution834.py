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
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build the tree as an adjacency list
        tree = {i: [] for i in range(n)}
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        # Initialize the result array and count array
        res = [0] * n
        count = [1] * n  # count[i] will hold the number of nodes in the subtree rooted at i
        
        def dfs1(node, parent):
            for child in tree[node]:
                if child != parent:
                    dfs1(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]
        
        def dfs2(node, parent):
            for child in tree[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs2(child, node)
        
        # First DFS to calculate the sum of distances for the root (node 0)
        dfs1(0, -1)
        
        # Second DFS to calculate the sum of distances for all nodes
        dfs2(0, -1)
        
        return res

def sumOfDistancesInTree(n: int, edges: List[List[int]]) -> List[int]:
    return Solution().sumOfDistancesInTree(n, edges)