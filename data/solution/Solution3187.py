import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Identify initial peaks
        peaks = set()
        n = len(nums)
        
        for i in range(1, n - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:
                peaks.add(i)
        
        def is_peak(index: int) -> bool:
            return nums[index - 1] < nums[index] > nums[index + 1]
        
        def update_peaks(index: int) -> None:
            # Remove the peak status of the affected elements
            if index - 1 in peaks:
                peaks.remove(index - 1)
            if index in peaks:
                peaks.remove(index)
            if index + 1 in peaks:
                peaks.remove(index + 1)
            
            # Update the peak status of the affected elements
            if index - 1 > 0 and is_peak(index - 1):
                peaks.add(index - 1)
            if index > 0 and index < n - 1 and is_peak(index):
                peaks.add(index)
            if index + 1 < n - 1 and is_peak(index + 1):
                peaks.add(index + 1)
        
        # Process the queries
        result = []
        for query in queries:
            if query[0] == 1:
                li, ri = query[1], query[2]
                # Count peaks in the subarray nums[li..ri]
                count = sum(1 for i in peaks if li < i < ri)
                result.append(count)
            elif query[0] == 2:
                indexi, vali = query[1], query[2]
                # Update the element and adjust peaks
                if nums[indexi] != vali:
                    nums[indexi] = vali
                    update_peaks(indexi)
        
        return result

def countOfPeaks(nums: List[int], queries: List[List[int]]) -> List[int]:
    return Solution().countOfPeaks(nums, queries)