import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # Get all unique characters
        unique_chars = set(''.join(words) + result)
        
        if len(unique_chars) > 10:
            return False
        
        # Characters that cannot be zero (they are the first character of a word or result)
        non_zero_chars = set([w[0] for w in words if len(w) > 1] + [result[0] if len(result) > 1 else ''])
        
        def solve(index, col, carry, char_to_digit, used_digits):
            # If we have processed all columns
            if col >= max(len(w) for w in words) and col >= len(result):
                return carry == 0
            
            # If we have processed all characters in the current column
            if index == len(words) + 1:
                # Calculate the sum of the column and the carry
                column_sum = sum(char_to_digit.get(w[-col-1], 0) for w in words if col < len(w)) + carry
                
                # Check if the last digit of the column sum matches the corresponding digit in the result
                if col < len(result) and column_sum % 10 == char_to_digit.get(result[-col-1], 0):
                    return solve(0, col + 1, column_sum // 10, char_to_digit, used_digits)
                else:
                    return False
            
            # Process each word or result
            if index < len(words) and col < len(words[index]):
                char = words[index][-col-1]
            elif col < len(result):
                char = result[-col-1]
            else:
                return solve(index + 1, col, carry, char_to_digit, used_digits)
            
            # If the character is already mapped to a digit
            if char in char_to_digit:
                return solve(index + 1, col, carry, char_to_digit, used_digits)
            
            # Try to map the character to a digit
            for digit in range(10):
                if digit not in used_digits and (digit != 0 or char not in non_zero_chars):
                    char_to_digit[char] = digit
                    used_digits.add(digit)
                    if solve(index + 1, col, carry, char_to_digit, used_digits):
                        return True
                    char_to_digit.pop(char)
                    used_digits.remove(digit)
            
            return False
        
        return solve(0, 0, 0, {}, set())

def isSolvable(words: List[str], result: str) -> bool:
    return Solution().isSolvable(words, result)