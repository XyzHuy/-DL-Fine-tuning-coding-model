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
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        # Build the adjacency list for the tree
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        # Initialize the result array with 1s
        coins = [1] * len(cost)
        
        # Helper function to perform DFS and return sorted costs of the subtree
        def dfs(node, parent):
            # Collect all costs in the subtree, starting with the current node's cost
            subtree_costs = [cost[node]]
            
            # Traverse the children
            for neighbor in tree[node]:
                if neighbor != parent:  # Avoid going back to the parent
                    subtree_costs.extend(dfs(neighbor, node))
            
            # Sort the costs to easily find the maximum product of three distinct nodes
            subtree_costs.sort()
            
            # If the subtree has 3 or more nodes, calculate the coins
            if len(subtree_costs) >= 3:
                # Calculate the product of the three largest costs
                max_product1 = subtree_costs[-1] * subtree_costs[-2] * subtree_costs[-3]
                
                # Also consider the product of the two smallest (potentially negative) and the largest cost
                max_product2 = subtree_costs[0] * subtree_costs[1] * subtree_costs[-1]
                
                # Place the maximum of the two products, or 0 if the product is negative
                coins[node] = max(max_product1, max_product2, 0)
            
            # Return the sorted costs of the subtree
            return subtree_costs
        
        # Start DFS from the root node 0
        dfs(0, -1)
        
        return coins

def placedCoins(edges: List[List[int]], cost: List[int]) -> List[int]:
    return Solution().placedCoins(edges, cost)