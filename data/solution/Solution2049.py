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
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        from collections import defaultdict
        
        # Build the tree using adjacency list
        tree = defaultdict(list)
        for i, parent in enumerate(parents):
            if parent != -1:
                tree[parent].append(i)
        
        # Dictionary to store the size of each subtree
        subtree_size = {}
        
        # Function to calculate the size of each subtree
        def calculate_size(node):
            if node not in tree:
                subtree_size[node] = 1
                return 1
            
            total_size = 1
            for child in tree[node]:
                total_size += calculate_size(child)
            
            subtree_size[node] = total_size
            return total_size
        
        # Calculate subtree sizes for all nodes
        total_nodes = calculate_size(0)
        
        # Function to calculate the score of each node
        def calculate_score(node):
            score = 1
            remaining_nodes = total_nodes - subtree_size[node] if node != 0 else 1
            
            for child in tree[node]:
                score *= subtree_size[child]
            
            if remaining_nodes > 0:
                score *= remaining_nodes
            
            return score
        
        # Calculate the score for each node and find the highest score
        max_score = 0
        max_count = 0
        for node in range(total_nodes):
            score = calculate_score(node)
            if score > max_score:
                max_score = score
                max_count = 1
            elif score == max_score:
                max_count += 1
        
        return max_count

def countHighestScoreNodes(parents: List[int]) -> int:
    return Solution().countHighestScoreNodes(parents)