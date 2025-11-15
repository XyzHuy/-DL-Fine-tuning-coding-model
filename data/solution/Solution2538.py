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
from collections import defaultdict
from typing import List

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        # Build the adjacency list for the tree
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, parent):
            # The maximum path sum including this node and extending to one of its children
            max_path_sum = 0
            # The second maximum path sum including this node and extending to one of its children
            second_max_path_sum = 0
            
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                child_max_path_sum, _ = dfs(neighbor, node)
                # Update the max and second max path sums
                if child_max_path_sum > max_path_sum:
                    second_max_path_sum = max_path_sum
                    max_path_sum = child_max_path_sum
                elif child_max_path_sum > second_max_path_sum:
                    second_max_path_sum = child_max_path_sum
            
            # The maximum path sum starting at this node and including its children
            max_start_here = max_path_sum + price[node]
            # The second maximum path sum starting at this node and including its children
            second_max_start_here = second_max_path_sum + price[node]
            
            return max_start_here, second_max_start_here
        
        max_cost = 0
        
        # Try rooting the tree at each node
        for i in range(n):
            max_start_here, second_max_start_here = dfs(i, -1)
            # The cost is the maximum path sum starting at this node minus the node's price
            max_cost = max(max_cost, max_start_here - price[i], second_max_start_here - price[i])
        
        return max_cost

def maxOutput(n: int, edges: List[List[int]], price: List[int]) -> int:
    return Solution().maxOutput(n, edges, price)