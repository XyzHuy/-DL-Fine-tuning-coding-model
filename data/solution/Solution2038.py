import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # Count the number of valid moves for Alice and Bob
        alice_moves = 0
        bob_moves = 0
        
        # Iterate through the string, starting from the second character and ending at the second to last character
        for i in range(1, len(colors) - 1):
            if colors[i] == 'A' and colors[i-1] == 'A' and colors[i+1] == 'A':
                alice_moves += 1
            elif colors[i] == 'B' and colors[i-1] == 'B' and colors[i+1] == 'B':
                bob_moves += 1
        
        # Alice wins if she has more valid moves than Bob
        return alice_moves > bob_moves

def winnerOfGame(colors: str) -> bool:
    return Solution().winnerOfGame(colors)