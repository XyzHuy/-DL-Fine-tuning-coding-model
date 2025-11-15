import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_and_count(nums, start, mid, end):
            count = 0
            left = nums[start:mid]
            right = nums[mid:end]
            i = j = 0
            k = start
            
            # Count reverse pairs
            while i < len(left) and j < len(right):
                if left[i] > 2 * right[j]:
                    count += (mid - start) - i
                    j += 1
                else:
                    i += 1
            
            # Merge the arrays
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
            
            return count
        
        def merge_sort_and_count(nums, start, end):
            if end - start <= 1:
                return 0
            mid = (start + end) // 2
            count = 0
            count += merge_sort_and_count(nums, start, mid)
            count += merge_sort_and_count(nums, mid, end)
            count += merge_and_count(nums, start, mid, end)
            return count
        
        return merge_sort_and_count(nums, 0, len(nums))

def reversePairs(nums: List[int]) -> int:
    return Solution().reversePairs(nums)