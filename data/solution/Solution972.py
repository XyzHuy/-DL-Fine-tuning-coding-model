import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        def parse_rational(rational: str):
            if '(' not in rational:
                return rational, ''
            
            non_repeating, repeating = rational.split('(')
            repeating = repeating.rstrip(')')
            return non_repeating, repeating
        
        def expand_rational(non_repeating: str, repeating: str, length: int = 100):
            if not repeating:
                return non_repeating
            
            if '.' in non_repeating:
                integer_part, decimal_part = non_repeating.split('.')
            else:
                integer_part, decimal_part = non_repeating, ''
            
            repeating_length = len(repeating)
            expanded_decimal_part = decimal_part + (repeating * (length // repeating_length + 1))[:length]
            return f"{integer_part}.{expanded_decimal_part}"
        
        def convert_to_float(rational: str):
            return float(expand_rational(*parse_rational(rational)))
        
        return abs(convert_to_float(s) - convert_to_float(t)) < 1e-9

# Example usage:
# sol = Solution()
# print(sol.isRationalEqual("0.(52)", "0.5(25)"))  # Output: True
# print(sol.isRationalEqual("0.1666(6)", "0.166(66)"))  # Output: True
# print(sol.isRationalEqual("0.9(9)", "1."))  # Output: True

def isRationalEqual(s: str, t: str) -> bool:
    return Solution().isRationalEqual(s, t)