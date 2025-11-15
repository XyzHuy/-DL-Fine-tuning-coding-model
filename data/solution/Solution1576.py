import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def modifyString(self, s: str) -> str:
        s_list = list(s)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        
        for i in range(len(s_list)):
            if s_list[i] == '?':
                # Determine the previous and next characters
                prev_char = s_list[i - 1] if i > 0 else ''
                next_char = s_list[i + 1] if i < len(s_list) - 1 else ''
                
                # Find a replacement character that is not equal to prev_char or next_char
                for char in alphabet:
                    if char != prev_char and char != next_char:
                        s_list[i] = char
                        break
        
        return ''.join(s_list)

def modifyString(s: str) -> str:
    return Solution().modifyString(s)