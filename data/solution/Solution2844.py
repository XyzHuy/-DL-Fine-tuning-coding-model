import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def minimumOperations(self, num: str) -> int:
        def find_last_digit(num, target, seen):
            for i in range(len(num) - 1, -1, -1):
                if num[i] == target:
                    return i, seen
                seen += 1
            return -1, seen
        
        min_operations = len(num)
        
        # Check for ending in '00'
        index_01, seen = find_last_digit(num, '0', 0)
        if index_01 != -1:
            index_02, seen = find_last_digit(num[:index_01], '0', seen)
            if index_02 != -1:
                min_operations = min(min_operations, seen)
        
        # Check for ending in '25'
        index_5, seen = find_last_digit(num, '5', 0)
        if index_5 != -1:
            index_2, seen = find_last_digit(num[:index_5], '2', seen)
            if index_2 != -1:
                min_operations = min(min_operations, seen)
        
        # Check for ending in '50'
        index_0, seen = find_last_digit(num, '0', 0)
        if index_0 != -1:
            index_5, seen = find_last_digit(num[:index_0], '5', seen)
            if index_5 != -1:
                min_operations = min(min_operations, seen)
        
        # Check for ending in '75'
        index_5, seen = find_last_digit(num, '5', 0)
        if index_5 != -1:
            index_7, seen = find_last_digit(num[:index_5], '7', seen)
            if index_7 != -1:
                min_operations = min(min_operations, seen)
        
        # If we found a '0', we can always make the number '0' which is divisible by 25
        if '0' in num:
            min_operations = min(min_operations, len(num) - 1)
        
        return min_operations

def minimumOperations(num: str) -> int:
    return Solution().minimumOperations(num)