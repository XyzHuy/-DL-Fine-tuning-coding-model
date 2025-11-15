import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        min_num = min(nums)
        max_num = max(nums)
        
        # If all numbers are the same, the maximum gap is 0
        if min_num == max_num:
            return 0
        
        # Bucket sort setup
        bucket_size = max(1, (max_num - min_num) // (n - 1))
        bucket_count = (max_num - min_num) // bucket_size + 1
        buckets = [{'min': float('inf'), 'max': float('-inf')} for _ in range(bucket_count)]
        
        # Distribute the numbers into buckets
        for num in nums:
            index = (num - min_num) // bucket_size
            buckets[index]['min'] = min(buckets[index]['min'], num)
            buckets[index]['max'] = max(buckets[index]['max'], num)
        
        # Find the maximum gap
        max_gap = 0
        prev_max = min_num
        
        for bucket in buckets:
            if bucket['min'] == float('inf'):
                continue  # Skip empty buckets
            max_gap = max(max_gap, bucket['min'] - prev_max)
            prev_max = bucket['max']
        
        return max_gap

def maximumGap(nums: List[int]) -> int:
    return Solution().maximumGap(nums)