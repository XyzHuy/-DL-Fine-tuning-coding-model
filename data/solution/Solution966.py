import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word):
            return ''.join('*' if c in 'aeiou' else c for c in word.lower())
        
        words = set(wordlist)
        words_lower = {}
        words_devowel = {}
        
        for word in wordlist:
            word_lower = word.lower()
            word_devowel = devowel(word)
            if word_lower not in words_lower:
                words_lower[word_lower] = word
            if word_devowel not in words_devowel:
                words_devowel[word_devowel] = word
        
        result = []
        
        for query in queries:
            if query in words:
                result.append(query)
            elif query.lower() in words_lower:
                result.append(words_lower[query.lower()])
            elif devowel(query) in words_devowel:
                result.append(words_devowel[devowel(query)])
            else:
                result.append('')
        
        return result

def spellchecker(wordlist: List[str], queries: List[str]) -> List[str]:
    return Solution().spellchecker(wordlist, queries)