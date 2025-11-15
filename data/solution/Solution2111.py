import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        def lengthOfLNDS(subseq):
            # This function calculates the length of the longest non-decreasing subsequence
            # using a variant of patience sorting.
            n = len(subseq)
            if n == 0:
                return 0
            
            # This will store the smallest tail of all increasing subsequences
            # with different lengths found so far.
            tails = []
            
            for num in subseq:
                # Use binary search to find the insertion point of the current number
                # in the tails array.
                idx = binary_search(tails, num)
                if idx == len(tails):
                    tails.append(num)
                else:
                    tails[idx] = num
            
            return len(tails)
        
        def binary_search(tails, num):
            # This function performs binary search to find the position to replace
            # or extend the tails array.
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] <= num:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        total_changes = 0
        n = len(arr)
        
        # For each starting index from 0 to k-1, form the subsequence and calculate
        # the number of changes needed to make it non-decreasing.
        for start in range(k):
            subseq = []
            for i in range(start, n, k):
                subseq.append(arr[i])
            lnds_length = lengthOfLNDS(subseq)
            total_changes += len(subseq) - lnds_length
        
        return total_changes

def kIncreasing(arr: List[int], k: int) -> int:
    return Solution().kIncreasing(arr, k)