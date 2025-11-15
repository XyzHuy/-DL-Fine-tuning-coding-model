import random
import functools
import collections
import string
import math
import datetime


from typing import List
import bisect

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        # Pair up nums1 and nums2 and sort by nums1 in descending order
        pairs = sorted(zip(nums1, nums2), reverse=True)
        n = len(pairs)
        
        # Sort queries by xi in descending order and keep track of original indices
        sorted_queries = sorted(enumerate(queries), key=lambda x: -x[1][0])
        
        # Result array to store the answers
        result = [-1] * len(queries)
        
        # List to keep track of (yi, sum) pairs
        active_pairs = []
        
        # Index to track the current position in the sorted pairs
        pair_index = 0
        
        for query_index, (xi, yi) in sorted_queries:
            # Add pairs that satisfy the xi constraint
            while pair_index < n and pairs[pair_index][0] >= xi:
                x, y = pairs[pair_index]
                s = x + y
                # Maintain the sorted list of (yi, sum) pairs
                # If y is less than or equal to the smallest yi in active_pairs, we can ignore it
                if not active_pairs or y > active_pairs[-1][0]:
                    # Remove elements that have a smaller or equal yi and a smaller or equal sum
                    while active_pairs and active_pairs[-1][0] <= y and active_pairs[-1][1] <= s:
                        active_pairs.pop()
                    # Add the current (y, s) pair
                    active_pairs.append((y, s))
                pair_index += 1
            
            # Use binary search to find the maximum sum that satisfies the yi constraint
            if active_pairs:
                # Find the first pair with yi' >= yi
                idx = bisect.bisect_left(active_pairs, (yi, float('-inf')))
                if idx < len(active_pairs):
                    result[query_index] = active_pairs[idx][1]
        
        return result

def maximumSumQueries(nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().maximumSumQueries(nums1, nums2, queries)