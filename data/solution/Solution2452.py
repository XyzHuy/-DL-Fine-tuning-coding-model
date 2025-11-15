import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def is_within_two_edits(word1: str, word2: str) -> bool:
            # Count the number of differing characters between word1 and word2
            edit_count = sum(1 for a, b in zip(word1, word2) if a != b)
            return edit_count <= 2
        
        result = []
        for query in queries:
            # Check if the query matches any word in the dictionary within two edits
            if any(is_within_two_edits(query, word) for word in dictionary):
                result.append(query)
        
        return result

def twoEditWords(queries: List[str], dictionary: List[str]) -> List[str]:
    return Solution().twoEditWords(queries, dictionary)