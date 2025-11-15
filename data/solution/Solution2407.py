import random
import functools
import collections
import string
import math
import datetime


from typing import List

class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)
    
    def update(self, index, value):
        self._update(0, 0, self.n - 1, index, value)
    
    def _update(self, node, start, end, index, value):
        if start == end:
            self.tree[node] = value
            return
        mid = (start + end) // 2
        if start <= index <= mid:
            self._update(2 * node + 1, start, mid, index, value)
        else:
            self._update(2 * node + 2, mid + 1, end, index, value)
        self.tree[node] = max(self.tree[2 * node + 1], self.tree[2 * node + 2])
    
    def query(self, left, right):
        return self._query(0, 0, self.n - 1, left, right)
    
    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return max(self._query(2 * node + 1, start, mid, left, right),
                   self._query(2 * node + 2, mid + 1, end, left, right))

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        segment_tree = SegmentTree(max_num + 1)
        result = 0
        
        for num in nums:
            # Find the maximum length of increasing subsequences ending in the range [num - k, num - 1]
            max_length = segment_tree.query(max(0, num - k), num - 1) + 1
            result = max(result, max_length)
            # Update the segment tree with the new length for the current number
            segment_tree.update(num, max_length)
        
        return result

def lengthOfLIS(nums: List[int], k: int) -> int:
    return Solution().lengthOfLIS(nums, k)