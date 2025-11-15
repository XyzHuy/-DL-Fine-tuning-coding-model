import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        
        # Count the frequency of each character in ransomNote and magazine
        note_count = Counter(ransomNote)
        magazine_count = Counter(magazine)
        
        # Check if magazine has enough of each character to construct ransomNote
        for char, count in note_count.items():
            if magazine_count[char] < count:
                return False
        
        return True

def canConstruct(ransomNote: str, magazine: str) -> bool:
    return Solution().canConstruct(ransomNote, magazine)