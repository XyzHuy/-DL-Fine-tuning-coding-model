import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        
        def is_valid_sequence(start: int, first: int, second: int) -> bool:
            if start == len(num):
                return True
            
            expected = first + second
            expected_str = str(expected)
            
            if num.startswith(expected_str, start):
                return is_valid_sequence(start + len(expected_str), second, expected)
            
            return False
        
        n = len(num)
        
        # The first number can be from index 0 to n-3 (inclusive)
        for i in range(1, n - 1):
            # The second number can be from index i to n-2 (inclusive)
            for j in range(i + 1, n):
                first_num = num[:i]
                second_num = num[i:j]
                
                # Check for leading zeros
                if (len(first_num) > 1 and first_num[0] == '0') or (len(second_num) > 1 and second_num[0] == '0'):
                    continue
                
                if is_valid_sequence(j, int(first_num), int(second_num)):
                    return True
        
        return False

def isAdditiveNumber(num: str) -> bool:
    return Solution().isAdditiveNumber(num)