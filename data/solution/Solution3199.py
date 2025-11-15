import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_even_odd_bits(arr):
            even_count = 0
            odd_count = 0
            for num in arr:
                if bin(num).count('1') % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
            return even_count, odd_count
        
        even_a, odd_a = count_even_odd_bits(a)
        even_b, odd_b = count_even_odd_bits(b)
        even_c, odd_c = count_even_odd_bits(c)
        
        total_triplets = (even_a * even_b * even_c) + \
                         (even_a * odd_b * odd_c) + \
                         (odd_a * even_b * odd_c) + \
                         (odd_a * odd_b * even_c)
        
        return total_triplets

def tripletCount(a: List[int], b: List[int], c: List[int]) -> int:
    return Solution().tripletCount(a, b, c)