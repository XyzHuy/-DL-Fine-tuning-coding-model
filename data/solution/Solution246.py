import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Mapping of digits to their strobogrammatic counterparts
        strobogrammatic_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        # Reverse the number and check if each digit maps correctly
        rotated = []
        for digit in reversed(num):
            if digit not in strobogrammatic_map:
                return False
            rotated.append(strobogrammatic_map[digit])
        
        # Join the rotated list to form the rotated number string
        rotated_num = ''.join(rotated)
        
        # Check if the original number is the same as the rotated number
        return num == rotated_num

def isStrobogrammatic(num: str) -> bool:
    return Solution().isStrobogrammatic(num)