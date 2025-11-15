import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def canAliceWin(self, a: List[str], b: List[str]) -> bool:
        # Alice starts with her smallest word
        ia, ib = 0, 0
        current_word = a[ia]
        ia += 1
        
        while True:
            # It's Bob's turn to play
            found = False
            while ib < len(b) and (b[ib] <= current_word or (b[ib][0] != current_word[0] and b[ib][0] != chr(ord(current_word[0]) + 1))):
                ib += 1
            if ib == len(b):
                # Bob can't play a word, Alice wins
                return True
            current_word = b[ib]
            ib += 1
            
            # It's Alice's turn to play
            found = False
            while ia < len(a) and (a[ia] <= current_word or (a[ia][0] != current_word[0] and a[ia][0] != chr(ord(current_word[0]) + 1))):
                ia += 1
            if ia == len(a):
                # Alice can't play a word, Bob wins
                return False
            current_word = a[ia]
            ia += 1

def canAliceWin(a: List[str], b: List[str]) -> bool:
    return Solution().canAliceWin(a, b)