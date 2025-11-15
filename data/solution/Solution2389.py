import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()  # Sort the nums array to consider the smallest elements first
        prefix_sum = [0] * (len(nums) + 1)
        
        # Create a prefix sum array
        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        answer = []
        
        # For each query, find the maximum size of the subsequence
        for query in queries:
            # Use binary search to find the rightmost index where the prefix sum is less than or equal to the query
            index = self.binarySearch(prefix_sum, query)
            answer.append(index - 1)  # Subtract 1 because prefix_sum is 1-based
        
        return answer
    
    def binarySearch(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left

def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
    return Solution().answerQueries(nums, queries)