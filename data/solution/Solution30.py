import random
import functools
import collections
import string
import math
import datetime


from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words or not words[0]:
            return []
        
        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result = []
        
        # Iterate over each possible starting point
        for i in range(word_length):
            left = i
            right = i
            current_count = Counter()
            
            while right + word_length <= len(s):
                word = s[right:right + word_length]
                right += word_length
                
                if word in word_count:
                    current_count[word] += 1
                    
                    while current_count[word] > word_count[word]:
                        current_count[s[left:left + word_length]] -= 1
                        left += word_length
                    
                    if right - left == total_length:
                        result.append(left)
                
                else:
                    current_count.clear()
                    left = right
        
        return result

def findSubstring(s: str, words: List[str]) -> List[int]:
    return Solution().findSubstring(s, words)