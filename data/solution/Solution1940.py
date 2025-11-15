import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import Counter

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        # Count the frequency of each number across all arrays
        frequency = Counter(num for arr in arrays for num in arr)
        
        # The common subsequence will consist of numbers that appear in all arrays
        # Since each array is sorted and strictly increasing, we can just check the length of arrays
        common_subsequence = [num for num, count in frequency.items() if count == len(arrays)]
        
        # Since the arrays are sorted, the common elements will also be in sorted order
        return common_subsequence

def longestCommonSubsequence(arrays: List[List[int]]) -> List[int]:
    return Solution().longestCommonSubsequence(arrays)