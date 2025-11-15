import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        # Check if it's possible to make nums1[n-1] and nums2[n-1] the maximum of their respective arrays
        max1 = max(nums1)
        max2 = max(nums2)
        
        # Function to check the number of swaps needed if we don't swap the last elements
        def count_swaps(last1, last2):
            swaps = 0
            for i in range(n - 1):
                if nums1[i] > last1 or nums2[i] > last2:
                    if nums1[i] > last2 or nums2[i] > last1:
                        return float('inf')  # Impossible to satisfy the conditions
                    swaps += 1
            return swaps
        
        # Check both scenarios: swapping the last elements or not swapping them
        swap_last = count_swaps(nums2[-1], nums1[-1]) + 1
        no_swap_last = count_swaps(nums1[-1], nums2[-1])
        
        # Get the minimum number of swaps
        result = min(swap_last, no_swap_last)
        
        # If result is infinity, it means it's impossible to satisfy the conditions
        return result if result != float('inf') else -1

def minOperations(nums1: List[int], nums2: List[int]) -> int:
    return Solution().minOperations(nums1, nums2)