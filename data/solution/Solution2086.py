import heapq
import itertools
from sortedcontainers import SortedList
import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        buckets = 0
        hamsters_list = list(hamsters)
        
        for i in range(n):
            if hamsters_list[i] == 'H':
                # Check if there's a bucket to the left
                if i > 0 and hamsters_list[i - 1] == 'B':
                    continue
                # Check if there's a bucket to the right
                elif i < n - 1 and hamsters_list[i + 1] == 'B':
                    continue
                # Place a bucket to the right if possible
                elif i < n - 1 and hamsters_list[i + 1] == '.':
                    hamsters_list[i + 1] = 'B'
                    buckets += 1
                # Place a bucket to the left if possible
                elif i > 0 and hamsters_list[i - 1] == '.':
                    hamsters_list[i - 1] = 'B'
                    buckets += 1
                # If neither left nor right is possible, return -1
                else:
                    return -1
        
        return buckets

def minimumBuckets(hamsters: str) -> int:
    return Solution().minimumBuckets(hamsters)