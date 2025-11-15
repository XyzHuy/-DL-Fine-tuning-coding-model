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
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Step 1: Build the tree
        tree = defaultdict(list)
        for u, v, w in edges:
            tree[u].append((v, w))
            tree[v].append((u, w))
        
        # Step 2: Precompute the path information using DFS
        # parent[i][j]: 2^j-th parent of node i
        # depth[i]: depth of node i
        # count[i][w]: number of edges of weight w on the path from root to node i
        LOG = 16  # log2(10000) + 1
        parent = [[-1] * LOG for _ in range(n)]
        depth = [0] * n
        count = [[0] * 27 for _ in range(n)]  # weights are from 1 to 26
        
        def dfs(node, par, d, edge_weight):
            parent[node][0] = par
            depth[node] = d
            if par != -1:
                count[node] = count[par][:]
            if edge_weight > 0:
                count[node][edge_weight] += 1
            
            for neighbor, weight in tree[node]:
                if neighbor != par:
                    dfs(neighbor, node, d + 1, weight)
        
        dfs(0, -1, 0, 0)  # Start DFS from the root node 0
        
        # Step 3: Binary lifting for LCA
        for j in range(1, LOG):
            for i in range(n):
                if parent[i][j - 1] != -1:
                    parent[i][j] = parent[parent[i][j - 1]][j - 1]
        
        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            # Step up u to the same depth as v
            for j in range(LOG - 1, -1, -1):
                if depth[u] - (1 << j) >= depth[v]:
                    u = parent[u][j]
            if u == v:
                return u
            # Step both u and v up until they meet at the LCA
            for j in range(LOG - 1, -1, -1):
                if parent[u][j] != parent[v][j]:
                    u = parent[u][j]
                    v = parent[v][j]
            return parent[u][0]
        
        # Step 4: Answer each query
        result = []
        for a, b in queries:
            l = lca(a, b)
            total_edges = (depth[a] - depth[l]) + (depth[b] - depth[l])
            max_weight_count = 0
            for w in range(1, 27):
                max_weight_count = max(max_weight_count, count[a][w] + count[b][w] - 2 * count[l][w])
            result.append(total_edges - max_weight_count)
        
        return result

def minOperationsQueries(n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    return Solution().minOperationsQueries(n, edges, queries)