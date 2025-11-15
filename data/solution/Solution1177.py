import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        # Create a prefix frequency array using bitmasks
        prefix_count = [0] * (len(s) + 1)
        
        for i, char in enumerate(s):
            # Toggle the bit corresponding to the current character
            prefix_count[i + 1] = prefix_count[i] ^ (1 << (ord(char) - ord('a')))
        
        result = []
        
        for left, right, k in queries:
            # XOR to get the bitmask of the substring s[left:right+1]
            bitmask = prefix_count[right + 1] ^ prefix_count[left]
            # Count the number of set bits (characters with odd frequencies)
            odd_count = bin(bitmask).count('1')
            # Check if we can make the substring a palindrome with up to k replacements
            result.append(odd_count // 2 <= k)
        
        return result

def canMakePaliQueries(s: str, queries: List[List[int]]) -> List[bool]:
    return Solution().canMakePaliQueries(s, queries)