import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        encrypted_string = []
        
        for i in range(n):
            # Calculate the new index in a cyclic manner
            new_index = (i + k) % n
            encrypted_string.append(s[new_index])
        
        return ''.join(encrypted_string)

def getEncryptedString(s: str, k: int) -> str:
    return Solution().getEncryptedString(s, k)