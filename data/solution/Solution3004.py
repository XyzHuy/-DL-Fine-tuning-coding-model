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
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        def dfs(a: int, fa: int) -> bool:
            ok = True
            for b in g[a]:
                if b != fa:
                    t = dfs(b, a)
                    ok = ok and colors[a] == colors[b] and t
                    size[a] += size[b]
            if ok:
                nonlocal ans
                ans = max(ans, size[a])
            return ok

        n = len(edges) + 1
        g = [[] for _ in range(n)]
        size = [1] * n
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        ans = 0
        dfs(0, -1)
        return ans

def maximumSubtreeSize(edges: List[List[int]], colors: List[int]) -> int:
    return Solution().maximumSubtreeSize(edges, colors)