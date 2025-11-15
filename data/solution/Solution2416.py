import random
import functools
import collections
import string
import math
import datetime


from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
    
    def sum_prefix_scores(self, word: str) -> int:
        score = 0
        node = self.root
        for char in word:
            node = node.children[char]
            score += node.prefix_count
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        answer = []
        for word in words:
            answer.append(trie.sum_prefix_scores(word))
        
        return answer

def sumPrefixScores(words: List[str]) -> List[int]:
    return Solution().sumPrefixScores(words)