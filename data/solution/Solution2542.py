import random
import functools
import collections
import string
import math
import datetime


from typing import List
import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # Pair up nums1 and nums2 and sort by nums2 in descending order
        paired = sorted(zip(nums1, nums2), key=lambda x: -x[1])
        
        # Initialize a min-heap to keep track of the smallest elements in nums1
        min_heap = []
        total_sum = 0
        
        # First, add the first k elements to the heap
        for i in range(k):
            total_sum += paired[i][0]
            heapq.heappush(min_heap, paired[i][0])
        
        # Calculate the initial score
        max_score = total_sum * paired[k-1][1]
        
        # Iterate over the remaining elements
        for i in range(k, len(paired)):
            # Remove the smallest element from the heap
            total_sum -= heapq.heappop(min_heap)
            # Add the current element to the heap and update the total sum
            total_sum += paired[i][0]
            heapq.heappush(min_heap, paired[i][0])
            # Calculate the score with the current minimum from nums2
            max_score = max(max_score, total_sum * paired[i][1])
        
        return max_score

def maxScore(nums1: List[int], nums2: List[int], k: int) -> int:
    return Solution().maxScore(nums1, nums2, k)