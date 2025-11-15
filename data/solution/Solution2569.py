import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        total_sum = sum(nums2)
        ones_count = sum(nums1)
        flip_state = [False] * (n + 1)  # To keep track of flip ranges
        
        result = []
        
        for query in queries:
            if query[0] == 1:
                l, r = query[1], query[2]
                flip_state[l] = not flip_state[l]
                if r + 1 < n:
                    flip_state[r + 1] = not flip_state[r + 1]
            elif query[0] == 2:
                p = query[1]
                current_flip_state = False
                current_ones = 0
                for i in range(n):
                    current_flip_state ^= flip_state[i]
                    if current_flip_state:
                        current_ones += 1 - nums1[i]
                    else:
                        current_ones += nums1[i]
                total_sum += current_ones * p
            elif query[0] == 3:
                result.append(total_sum)
        
        return result

def handleQuery(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().handleQuery(nums1, nums2, queries)