import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        
        # Function to calculate the sum of digits of a number
        def sum_of_digits(num):
            return sum(int(digit) for digit in str(num))
        
        # Dictionary to store the size of each group
        group_sizes = defaultdict(int)
        
        # Group numbers by the sum of their digits
        for i in range(1, n + 1):
            digit_sum = sum_of_digits(i)
            group_sizes[digit_sum] += 1
        
        # Find the maximum size of the groups
        max_size = max(group_sizes.values())
        
        # Count how many groups have the maximum size
        largest_groups_count = sum(1 for size in group_sizes.values() if size == max_size)
        
        return largest_groups_count

def countLargestGroup(n: int) -> int:
    return Solution().countLargestGroup(n)