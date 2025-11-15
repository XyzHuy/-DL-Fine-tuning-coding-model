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

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        pp, pq = self.find(p), self.find(q)
        if pp == pq:
            return
        if self.rank[pp] < self.rank[pq]:
            pp, pq = pq, pp
        self.parent[pq] = pp
        self.rank[pp] += self.rank[pq]

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        uf = UnionFind(n)
        
        # Create a graph and a map from value to nodes with that value
        graph = defaultdict(list)
        value_to_nodes = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for i, val in enumerate(vals):
            value_to_nodes[val].append(i)
        
        # Process nodes in the order of their values
        sorted_values = sorted(set(vals))
        result = 0
        
        for val in sorted_values:
            # Union the nodes with the same value and their neighbors if the neighbor's value is less than or equal to the current value
            for node in value_to_nodes[val]:
                for neighbor in graph[node]:
                    if vals[neighbor] <= val:
                        uf.union(node, neighbor)
            
            # Count the number of nodes with the same value in each connected component
            component_count = defaultdict(int)
            for node in value_to_nodes[val]:
                root = uf.find(node)
                component_count[root] += 1
            
            # For each component, the number of good paths is the number of ways to choose 2 nodes from the component plus the number of single node paths
            for count in component_count.values():
                result += (count * (count + 1)) // 2
        
        return result

def numberOfGoodPaths(vals: List[int], edges: List[List[int]]) -> int:
    return Solution().numberOfGoodPaths(vals, edges)