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
from collections import defaultdict, Counter
from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        # Initialize the result array
        result = [0] * n
        
        def dfs(node: int, parent: int) -> Counter:
            # Count the labels in the current subtree
            count = Counter()
            
            # Traverse all children of the current node
            for neighbor in tree[node]:
                if neighbor != parent:
                    # Recursively count labels in the subtree rooted at the child
                    count += dfs(neighbor, node)
            
            # Count the current node's label
            count[labels[node]] += 1
            
            # Store the count of the current node's label in the result array
            result[node] = count[labels[node]]
            
            return count
        
        # Start DFS from the root node (node 0)
        dfs(0, -1)
        
        return result

def countSubTrees(n: int, edges: List[List[int]], labels: str) -> List[int]:
    return Solution().countSubTrees(n, edges, labels)