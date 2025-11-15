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
from math import inf
from typing import List

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        def dfs(i, fa, x):
            res = nums[i]
            for j in g[i]:
                if j != fa and j != x:
                    res ^= dfs(j, i, x)
            return res

        def dfs2(i, fa, x):
            nonlocal s, s1, ans
            res = nums[i]
            for j in g[i]:
                if j != fa and j != x:
                    a = dfs2(j, i, x)
                    res ^= a
                    b = s1 ^ a
                    c = s ^ s1
                    t = max(a, b, c) - min(a, b, c)
                    ans = min(ans, t)
            return res

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        s = 0
        for v in nums:
            s ^= v
        n = len(nums)
        ans = inf
        for i in range(n):
            for j in g[i]:
                s1 = dfs(i, -1, j)
                dfs2(i, -1, j)
        return ans

def minimumScore(nums: List[int], edges: List[List[int]]) -> int:
    return Solution().minimumScore(nums, edges)