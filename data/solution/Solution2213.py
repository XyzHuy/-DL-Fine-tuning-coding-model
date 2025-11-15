import random
import functools
import collections
import string
import math
import datetime


from typing import List

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.max_len = 0
        self.prefix_len = 0
        self.suffix_len = 0
        self.total_len = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, s):
        self.s = s
        self.root = self.build(0, len(s) - 1)
    
    def build(self, start, end):
        if start > end:
            return None
        node = SegmentTreeNode(start, end)
        if start == end:
            node.max_len = 1
            node.prefix_len = 1
            node.suffix_len = 1
            node.total_len = 1
            return node
        mid = (start + end) // 2
        node.left = self.build(start, mid)
        node.right = self.build(mid + 1, end)
        self.merge(node, node.left, node.right)
        return node
    
    def merge(self, node, left, right):
        if not left or not right:
            return
        node.total_len = left.total_len + right.total_len
        if self.s[left.end] == self.s[right.start]:
            node.prefix_len = left.prefix_len
            if left.prefix_len == left.total_len:
                node.prefix_len += right.prefix_len
            node.suffix_len = right.suffix_len
            if right.suffix_len == right.total_len:
                node.suffix_len += left.suffix_len
            node.max_len = max(left.max_len, right.max_len, left.suffix_len + right.prefix_len)
        else:
            node.prefix_len = left.prefix_len
            node.suffix_len = right.suffix_len
            node.max_len = max(left.max_len, right.max_len)
    
    def update(self, index, char):
        def _update(node, start, end, index, char):
            if start == end:
                self.s[index] = char
                return
            mid = (start + end) // 2
            if index <= mid:
                _update(node.left, start, mid, index, char)
            else:
                _update(node.right, mid + 1, end, index, char)
            self.merge(node, node.left, node.right)
        
        _update(self.root, 0, len(self.s) - 1, index, char)
    
    def query(self):
        return self.root.max_len

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        segment_tree = SegmentTree(list(s))
        result = []
        for char, index in zip(queryCharacters, queryIndices):
            segment_tree.update(index, char)
            result.append(segment_tree.query())
        return result

def longestRepeating(s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
    return Solution().longestRepeating(s, queryCharacters, queryIndices)