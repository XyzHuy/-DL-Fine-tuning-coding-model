import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        max_good = 0
        
        # Function to check if a given bitmask is valid
        def is_valid(combination):
            for i in range(n):
                if combination & (1 << i):  # If person i is good
                    for j in range(n):
                        if statements[i][j] == 0 and (combination & (1 << j)):  # Person i says j is bad, but j is good
                            return False
                        if statements[i][j] == 1 and not (combination & (1 << j)):  # Person i says j is good, but j is bad
                            return False
            return True
        
        # Try all possible combinations
        for combination in range(1 << n):  # 2^n possible combinations
            if is_valid(combination):
                count_good = bin(combination).count('1')  # Count number of good people
                max_good = max(max_good, count_good)
        
        return max_good

def maximumGood(statements: List[List[int]]) -> int:
    return Solution().maximumGood(statements)