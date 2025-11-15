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
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict
        
        # Build the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)
        
        # Function to find the diameter of a subtree rooted at 'root'
        def find_diameter(subtree):
            def dfs(node, parent):
                nonlocal max_diameter
                first_max = second_max = 0
                for neighbor in graph[node]:
                    if neighbor in subtree and neighbor != parent:
                        dist = dfs(neighbor, node) + 1
                        if dist > first_max:
                            second_max = first_max
                            first_max = dist
                        elif dist > second_max:
                            second_max = dist
                max_diameter = max(max_diameter, first_max + second_max)
                return first_max
            
            max_diameter = 0
            dfs(root, -1)
            return max_diameter
        
        # Generate all possible subtrees
        result = [0] * (n - 1)
        for i in range(1 << n):
            subtree = {j for j in range(n) if (i & (1 << j))}
            if len(subtree) < 2:
                continue
            
            # Find the root of the subtree
            for root in subtree:
                if all(neighbor in subtree for neighbor in graph[root]):
                    break
            
            # Check if the subset forms a connected subtree
            visited = set()
            def is_connected(node):
                if node in visited:
                    return
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor in subtree:
                        is_connected(neighbor)
            
            is_connected(root)
            if visited == subtree:
                diameter = find_diameter(subtree)
                if diameter > 0:
                    result[diameter - 1] += 1
        
        return result

def countSubgraphsForEachDiameter(n: int, edges: List[List[int]]) -> List[int]:
    return Solution().countSubgraphsForEachDiameter(n, edges)