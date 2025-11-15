import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        def count_partitions(s, k):
            partitions = 0
            char_set = set()
            for char in s:
                if len(char_set) < k or char in char_set:
                    char_set.add(char)
                else:
                    partitions += 1
                    char_set = set(char)
            partitions += 1  # Count the last partition
            return partitions
        
        max_partitions = count_partitions(s, k)
        n = len(s)
        
        for i in range(n):
            for new_char in 'abcdefghijklmnopqrstuvwxyz':
                if new_char != s[i]:
                    new_s = s[:i] + new_char + s[i+1:]
                    max_partitions = max(max_partitions, count_partitions(new_s, k))
        
        return max_partitions

def maxPartitionsAfterOperations(s: str, k: int) -> int:
    return Solution().maxPartitionsAfterOperations(s, k)