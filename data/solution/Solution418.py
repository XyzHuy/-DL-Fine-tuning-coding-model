import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        # Join the sentence into a single string with spaces and add a final space
        s = ' '.join(sentence) + ' '
        s_len = len(s)
        
        # Current position in the string
        start = 0
        
        for _ in range(rows):
            # Move start to the end of the current row
            start += cols
            
            # If we can fit another word, move start to the next word
            if s[start % s_len] == ' ':
                start += 1
            else:
                # Otherwise, move back to the last space before the current position
                while start > 0 and s[(start - 1) % s_len] != ' ':
                    start -= 1
        
        # The number of times the sentence fits is the number of full cycles
        return start // s_len

def wordsTyping(sentence: List[str], rows: int, cols: int) -> int:
    return Solution().wordsTyping(sentence, rows, cols)