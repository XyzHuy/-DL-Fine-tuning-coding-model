import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # Helper function to check if target_sub is a subsequence of source
        def is_subsequence(target_sub):
            it = iter(source)
            return all(char in it for char in target_sub)
        
        # If any character in target is not in source, it's impossible to form target
        if not set(target).issubset(set(source)):
            return -1
        
        count = 0
        i = 0
        
        while i < len(target):
            # Try to find the longest subsequence in source that matches the remaining part of target
            j = i
            while j < len(target) and is_subsequence(target[i:j+1]):
                j += 1
            
            # If j didn't move, it means no valid subsequence was found starting at i
            if j == i:
                return -1
            
            # Increment count for the found subsequence
            count += 1
            # Move i to the end of the last found subsequence
            i = j
        
        return count

def shortestWay(source: str, target: str) -> int:
    return Solution().shortestWay(source, target)