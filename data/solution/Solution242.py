import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths of the strings are not the same, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Create a dictionary to count the frequency of each character in s
        char_count = {}
        
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Decrease the count based on characters in t
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False
        
        # If all counts are zero, then t is an anagram of s
        return all(count == 0 for count in char_count.values())

def isAnagram(s: str, t: str) -> bool:
    return Solution().isAnagram(s, t)