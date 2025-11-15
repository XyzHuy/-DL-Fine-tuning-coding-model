import random
import functools
import collections
import string
import math
import datetime


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, w):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.is_end = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(w, start=0):
            if start == len(w):
                return True
            node = trie
            for i in range(start, len(w)):
                idx = ord(w[i]) - ord('a')
                if node.children[idx] is None:
                    return False
                node = node.children[idx]
                if node.is_end and dfs(w, i + 1):
                    return True
            return False

        trie = Trie()
        ans = []
        words.sort(key=lambda x: len(x))
        for w in words:
            if w:  # Ensure the word is not empty
                if dfs(w):
                    ans.append(w)
                else:
                    trie.insert(w)
        return ans

def findAllConcatenatedWordsInADict(words: List[str]) -> List[str]:
    return Solution().findAllConcatenatedWordsInADict(words)