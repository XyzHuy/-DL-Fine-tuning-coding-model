import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case: the first row is always 0
        if n == 1:
            return 0
        
        # Find the length of the (n-1)th row
        length_of_prev_row = 2 ** (n - 2)
        
        # If k is in the first half of the nth row, it is the same as the (k)th element of the (n-1)th row
        if k <= length_of_prev_row:
            return self.kthGrammar(n - 1, k)
        else:
            # If k is in the second half, it is the complement of the (k - length_of_prev_row)th element of the (n-1)th row
            return 1 - self.kthGrammar(n - 1, k - length_of_prev_row)

def kthGrammar(n: int, k: int) -> int:
    return Solution().kthGrammar(n, k)