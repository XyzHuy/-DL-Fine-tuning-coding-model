import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def get_prefixes(num):
            prefixes = set()
            s = str(num)
            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])
            return prefixes
        
        # Generate all prefixes for each number in arr1
        prefixes1 = set()
        for num in arr1:
            prefixes1.update(get_prefixes(num))
        
        # Generate all prefixes for each number in arr2
        prefixes2 = set()
        for num in arr2:
            prefixes2.update(get_prefixes(num))
        
        # Find the longest common prefix
        longest_common_prefix_length = 0
        for prefix in prefixes1:
            if prefix in prefixes2:
                longest_common_prefix_length = max(longest_common_prefix_length, len(prefix))
        
        return longest_common_prefix_length

def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
    return Solution().longestCommonPrefix(arr1, arr2)