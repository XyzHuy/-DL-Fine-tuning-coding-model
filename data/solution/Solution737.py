import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict, deque

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        # Build the graph
        graph = defaultdict(list)
        for x, y in similarPairs:
            graph[x].append(y)
            graph[y].append(x)
        
        # BFS to find if two words are similar
        def areSimilar(word1, word2):
            if word1 == word2:
                return True
            visited = set()
            queue = deque([word1])
            while queue:
                current = queue.popleft()
                if current == word2:
                    return True
                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            return False
        
        # Check each pair of words in the sentences
        for w1, w2 in zip(sentence1, sentence2):
            if not areSimilar(w1, w2):
                return False
        
        return True

def areSentencesSimilarTwo(sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
    return Solution().areSentencesSimilarTwo(sentence1, sentence2, similarPairs)