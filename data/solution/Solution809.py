import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def compress(word):
            if not word:
                return []
            compressed = []
            count = 1
            for i in range(1, len(word)):
                if word[i] == word[i - 1]:
                    count += 1
                else:
                    compressed.append((word[i - 1], count))
                    count = 1
            compressed.append((word[-1], count))
            return compressed
        
        s_compressed = compress(s)
        stretchy_count = 0
        
        for word in words:
            word_compressed = compress(word)
            if len(word_compressed) != len(s_compressed):
                continue
            
            stretchy = True
            for (sc, s_count), (wc, w_count) in zip(s_compressed, word_compressed):
                if sc != wc or (s_count < w_count) or (s_count < 3 and s_count != w_count):
                    stretchy = False
                    break
            
            if stretchy:
                stretchy_count += 1
        
        return stretchy_count

def expressiveWords(s: str, words: List[str]) -> int:
    return Solution().expressiveWords(s, words)