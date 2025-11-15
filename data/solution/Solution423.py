import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def originalDigits(self, s: str) -> str:
        from collections import Counter
        
        # Count the frequency of each character in the input string
        count = Counter(s)
        
        # Initialize a list to keep track of the count of each digit
        digits = [0] * 10
        
        # Identify unique characters for specific digits
        digits[0] = count['z']  # 'z' is unique to "zero"
        digits[2] = count['w']  # 'w' is unique to "two"
        digits[4] = count['u']  # 'u' is unique to "four"
        digits[6] = count['x']  # 'x' is unique to "six"
        digits[8] = count['g']  # 'g' is unique to "eight"
        
        # Identify characters that can be determined after removing the unique ones
        digits[3] = count['h'] - digits[8]  # 'h' is unique to "three" after removing "eight"
        digits[5] = count['f'] - digits[4]  # 'f' is unique to "five" after removing "four"
        digits[7] = count['s'] - digits[6]  # 's' is unique to "seven" after removing "six"
        digits[1] = count['o'] - (digits[0] + digits[2] + digits[4])  # 'o' is unique to "one" after removing "zero", "two", "four"
        digits[9] = count['i'] - (digits[5] + digits[6] + digits[8])  # 'i' is unique to "nine" after removing "five", "six", "eight"
        
        # Construct the result string by repeating each digit according to its count
        result = []
        for i in range(10):
            result.append(str(i) * digits[i])
        
        return ''.join(result)

def originalDigits(s: str) -> str:
    return Solution().originalDigits(s)