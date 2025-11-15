import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # Count odd and even numbers in the range [1, n]
        odd_n = (n + 1) // 2
        even_n = n // 2
        
        # Count odd and even numbers in the range [1, m]
        odd_m = (m + 1) // 2
        even_m = m // 2
        
        # Calculate the number of valid pairs (x, y)
        # where x is odd and y is even, or x is even and y is odd
        valid_pairs = (odd_n * even_m) + (even_n * odd_m)
        
        return valid_pairs

def flowerGame(n: int, m: int) -> int:
    return Solution().flowerGame(n, m)