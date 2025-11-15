import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        # Create a graph for synonyms
        graph = defaultdict(set)
        for word1, word2 in synonyms:
            graph[word1].add(word2)
            graph[word2].add(word1)
        
        # Create a dictionary to store the set of synonyms for each word
        synsets = defaultdict(set)
        
        # Function to perform DFS and find all synonyms for a word
        def dfs(word, synset):
            if word in synset:
                return
            synset.add(word)
            for neighbor in graph[word]:
                dfs(neighbor, synset)
        
        # Populate the synsets dictionary
        for word in graph:
            if word not in synsets:
                current_synset = set()
                dfs(word, current_synset)
                for syn in current_synset:
                    synsets[syn] = current_synset
        
        # Split the text into words
        words = text.split()
        
        # Generate all possible sentences
        def backtrack(index, path):
            if index == len(words):
                result.append(' '.join(path))
                return
            word = words[index]
            if word in synsets:
                for synonym in sorted(synsets[word]):
                    backtrack(index + 1, path + [synonym])
            else:
                backtrack(index + 1, path + [word])
        
        result = []
        backtrack(0, [])
        return sorted(result)

def generateSentences(synonyms: List[List[str]], text: str) -> List[str]:
    return Solution().generateSentences(synonyms, text)