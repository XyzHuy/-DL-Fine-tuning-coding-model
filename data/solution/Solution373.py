import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []
        
        min_heap = []
        # Initialize the heap with the first pair from nums1 and each element from nums2
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
        
        result = []
        # Extract the smallest pairs from the heap
        while k > 0 and min_heap:
            sum_val, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            k -= 1
            # If there are more elements in nums2, push the next pair from nums1[i] and nums2[j+1]
            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result

def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    return Solution().kSmallestPairs(nums1, nums2, k)