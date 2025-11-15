import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def generate_palindrome(half, is_odd):
            half_str = str(half)
            if is_odd:
                return int(half_str + half_str[-2::-1])
            else:
                return int(half_str + half_str[::-1])
        
        half_length = (intLength + 1) // 2
        start = 10**(half_length - 1)
        end = 10**half_length - 1
        is_odd = intLength % 2 == 1
        
        result = []
        for query in queries:
            half_number = start + query - 1
            if half_number > end:
                result.append(-1)
            else:
                result.append(generate_palindrome(half_number, is_odd))
        
        return result

def kthPalindrome(queries: List[int], intLength: int) -> List[int]:
    return Solution().kthPalindrome(queries, intLength)