import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def intToRoman(self, num: int) -> str:
        # Define a list of tuples that map integers to their corresponding Roman numeral strings
        val = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        # Initialize an empty string to build the Roman numeral
        roman_numeral = ""
        
        # Iterate over the value-symbol pairs
        for (integer, symbol) in val:
            # Determine how many times the symbol can fit into the remaining number
            count = num // integer
            # Append the symbol 'count' times to the result
            roman_numeral += symbol * count
            # Reduce the number by the equivalent integer value
            num -= integer * count
        
        return roman_numeral

def intToRoman(num: int) -> str:
    return Solution().intToRoman(num)