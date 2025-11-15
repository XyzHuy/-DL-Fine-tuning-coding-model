import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict
import math

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        
        # Function to compute the minimum operations to make all elements equal to the median
        def min_operations_to_median(nums):
            nums.sort()
            median = nums[len(nums) // 2]
            return sum(abs(num - median) for num in nums)
        
        # Group elements into connected components based on k
        visited = [False] * n
        total_operations = 0
        
        for i in range(n):
            if not visited[i]:
                component = []
                j = i
                while not visited[j]:
                    visited[j] = True
                    component.append(arr[j])
                    j = (j + k) % n
                total_operations += min_operations_to_median(component)
        
        return total_operations

def makeSubKSumEqual(arr: List[int], k: int) -> int:
    return Solution().makeSubKSumEqual(arr, k)