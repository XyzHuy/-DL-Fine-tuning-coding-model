import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # Combine k1 and k2 since they are equivalent in terms of operations
        k = k1 + k2
        
        # Calculate the absolute differences
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        # If k is 0, we cannot modify the arrays
        if k == 0:
            return sum(d ** 2 for d in diffs)
        
        # Count the frequency of each difference
        from collections import Counter
        diff_count = Counter(diffs)
        max_diff = max(diff_count.keys())
        
        # Use a max-heap to always reduce the largest difference first
        import heapq
        heap = [-d for d in diff_count.keys()]
        heapq.heapify(heap)
        
        while k > 0 and heap:
            largest_diff = -heapq.heappop(heap)
            
            # If the next largest difference is 0, we can't reduce further
            if largest_diff == 0:
                break
            
            # Determine how many occurrences of this difference we can reduce
            count = diff_count[largest_diff]
            if count <= k:
                # Reduce all occurrences of this difference
                k -= count
                del diff_count[largest_diff]
                
                # If there is a next smaller difference, increase its count
                if largest_diff - 1 > 0:
                    if largest_diff - 1 not in diff_count:
                        diff_count[largest_diff - 1] = 0
                        heapq.heappush(heap, -(largest_diff - 1))
                    diff_count[largest_diff - 1] += count
            else:
                # Reduce only k occurrences of this difference
                diff_count[largest_diff] -= k
                if largest_diff - 1 not in diff_count:
                    diff_count[largest_diff - 1] = 0
                    heapq.heappush(heap, -(largest_diff - 1))
                diff_count[largest_diff - 1] += k
                k = 0
        
        # Calculate the resulting sum of squared differences
        return sum(d ** 2 * count for d, count in diff_count.items())

def minSumSquareDiff(nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
    return Solution().minSumSquareDiff(nums1, nums2, k1, k2)