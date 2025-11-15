import random
import functools
import collections
import string
import math
import datetime


from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord is not in wordList, return 0
        if endWord not in wordList:
            return 0
        
        # Create a dictionary to hold the intermediate words
        adj_list = defaultdict(list)
        L = len(beginWord)
        
        # Create patterns like 'h*t' for each word in the list
        for word in wordList:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                adj_list[pattern].append(word)
        
        # BFS initialization
        visited = set([beginWord])
        q = deque([(beginWord, 1)])  # (current_word, current_length_of_sequence)
        
        while q:
            current_word, length = q.popleft()
            
            # Check all intermediate states of the current word
            for i in range(L):
                pattern = current_word[:i] + '*' + current_word[i+1:]
                for word in adj_list[pattern]:
                    if word == endWord:
                        return length + 1
                    if word not in visited:
                        visited.add(word)
                        q.append((word, length + 1))
        
        return 0

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    return Solution().ladderLength(beginWord, endWord, wordList)