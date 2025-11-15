import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number in nums
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        
        # Step 2: Create a list of buckets where index is the frequency
        # and the value is a list of numbers with that frequency
        max_frequency = max(frequency_map.values())
        buckets = [[] for _ in range(max_frequency + 1)]
        
        for num, freq in frequency_map.items():
            buckets[freq].append(num)
        
        # Step 3: Collect the top k frequent elements
        top_k_frequent_elements = []
        for freq in range(max_frequency, 0, -1):
            for num in buckets[freq]:
                top_k_frequent_elements.append(num)
                if len(top_k_frequent_elements) == k:
                    return top_k_frequent_elements

# Example usage:
# sol = Solution()
# print(sol.topKFrequent([1,1,1,2,2,3], 2))  # Output: [1, 2]
# print(sol.topKFrequent([1], 1))            # Output: [1]

def topKFrequent(nums: List[int], k: int) -> List[int]:
    return Solution().topKFrequent(nums, k)