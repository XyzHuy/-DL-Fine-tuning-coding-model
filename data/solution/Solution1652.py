import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        decrypted_code = [0] * n
        
        if k == 0:
            return decrypted_code
        
        for i in range(n):
            if k > 0:
                decrypted_code[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
            else:
                decrypted_code[i] = sum(code[(i - j) % n] for j in range(1, -k + 1))
        
        return decrypted_code

def decrypt(code: List[int], k: int) -> List[int]:
    return Solution().decrypt(code, k)