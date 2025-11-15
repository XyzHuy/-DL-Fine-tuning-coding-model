import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words or not groups:
            return []
        
        result = [words[0]]
        last_group = groups[0]
        
        for i in range(1, len(groups)):
            if groups[i] != last_group:
                result.append(words[i])
                last_group = groups[i]
        
        return result

def getLongestSubsequence(words: List[str], groups: List[int]) -> List[str]:
    return Solution().getLongestSubsequence(words, groups)