import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def count_unique_digits(num_str):
            length = len(num_str)
            # Count numbers with unique digits of length < len(num_str)
            unique_count = 0
            for i in range(1, length):
                unique_count += 9 * perm(9, i - 1)
            
            # Count numbers with unique digits of length == len(num_str)
            seen = set()
            for i, digit in enumerate(num_str):
                for d in range(0 if i else 1, int(digit)):
                    if d in seen:
                        continue
                    unique_count += perm(10 - i - 1, length - i - 1)
                if int(digit) in seen:
                    break
                seen.add(int(digit))
            else:
                unique_count += 1  # Include the number itself if all digits are unique
            
            return unique_count
        
        def perm(m, n):
            if n == 0:
                return 1
            return m * perm(m - 1, n - 1)
        
        num_str = str(n)
        total_numbers = int(num_str)
        unique_digit_numbers = count_unique_digits(num_str)
        return total_numbers - unique_digit_numbers

def numDupDigitsAtMostN(n: int) -> int:
    return Solution().numDupDigitsAtMostN(n)