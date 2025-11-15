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
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        def dfs(i: int, fa: int = -1) -> (int, int):
            a = b = 0
            leaf = True
            for j in g[i]:
                if j != fa:
                    leaf = False
                    aa, bb = dfs(j, i)
                    a += aa
                    b += bb
            if leaf:
                return values[i], 0
            return values[i] + a, max(values[i] + b, a)

        g = [[] for _ in range(len(values))]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        return dfs(0)[1]

def maximumScoreAfterOperations(edges: List[List[int]], values: List[int]) -> int:
    return Solution().maximumScoreAfterOperations(edges, values)