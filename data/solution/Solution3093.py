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
        self.index = -1  # Index of the word in wordsContainer
        self.length = float('inf')  # Length of the word

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        
        # Insert all words in wordsContainer into the suffix trie
        for i, word in enumerate(wordsContainer):
            node = root
            word_length = len(word)
            if word_length < node.length:
                node.index = i
                node.length = word_length
            for j in range(word_length - 1, -1, -1):
                char = word[j]
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
                if word_length < node.length:
                    node.index = i
                    node.length = word_length
        
        # For each query, find the longest common suffix
        result = []
        for query in wordsQuery:
            node = root
            for j in range(len(query) - 1, -1, -1):
                char = query[j]
                if char in node.children:
                    node = node.children[char]
                else:
                    break
            result.append(node.index)
        
        return result

# Example usage:
# sol = Solution()
# print(sol.stringIndices(["abcd","bcd","xbcd"], ["cd","bcd","xyz"]))  # Output: [1, 1, 1]
# print(sol.stringIndices(["abcdefgh","poiuygh","ghghgh"], ["gh","acbfgh","acbfegh"]))  # Output: [2, 0, 2]

def stringIndices(wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
    return Solution().stringIndices(wordsContainer, wordsQuery)