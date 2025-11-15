import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        def count_odd_parity(arr):
            return sum(1 for x in arr if x.bit_count() % 2 != 0)
        
        # Count odd and even parity elements in each array
        odd_a = count_odd_parity(a)
        even_a = len(a) - odd_a
        
        odd_b = count_odd_parity(b)
        even_b = len(b) - odd_b
        
        odd_c = count_odd_parity(c)
        even_c = len(c) - odd_c
        
        # Calculate the number of valid triplets
        # Case 1: All three numbers have even parity
        valid_triplets = even_a * even_b * even_c
        
        # Case 2: Exactly two numbers have odd parity, and one has even parity
        valid_triplets += (odd_a * odd_b * even_c) + (odd_a * even_b * odd_c) + (even_a * odd_b * odd_c)
        
        return valid_triplets

def tripletCount(a: List[int], b: List[int], c: List[int]) -> int:
    return Solution().tripletCount(a, b, c)