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
    def longestPath(self, parent: List[int], s: str) -> int:
        from collections import defaultdict
        
        # Build the tree as an adjacency list
        tree = defaultdict(list)
        for i in range(1, len(parent)):
            tree[parent[i]].append(i)
        
        # Global variable to keep track of the longest path
        self.ans = 1
        
        def dfs(node):
            # Longest and second longest chains starting from this node
            longest, second_longest = 0, 0
            for neighbor in tree[node]:
                neighbor_length = dfs(neighbor)
                # We only consider chains where the neighbor has a different character
                if s[neighbor] != s[node]:
                    # Update the two longest chains
                    if neighbor_length > longest:
                        second_longest = longest
                        longest = neighbor_length
                    elif neighbor_length > second_longest:
                        second_longest = neighbor_length
            
            # Update the answer considering the current node as the highest point of the "V" shaped path
            self.ans = max(self.ans, longest + second_longest + 1)
            
            # The longest chain including the current node as an endpoint
            return longest + 1
        
        dfs(0)
        return self.ans

def longestPath(parent: List[int], s: str) -> int:
    return Solution().longestPath(parent, s)