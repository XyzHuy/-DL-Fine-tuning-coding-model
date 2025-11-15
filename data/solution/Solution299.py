import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import defaultdict
        
        bulls = 0
        cows = 0
        secret_count = defaultdict(int)
        guess_count = defaultdict(int)
        
        # First pass to count bulls and potential cows
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] += 1
                guess_count[g] += 1
        
        # Calculate cows based on the counts
        for digit in secret_count:
            if digit in guess_count:
                cows += min(secret_count[digit], guess_count[digit])
        
        return f"{bulls}A{cows}B"

def getHint(secret: str, guess: str) -> str:
    return Solution().getHint(secret, guess)