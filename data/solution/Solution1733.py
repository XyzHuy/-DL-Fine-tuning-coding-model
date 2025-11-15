import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        # Convert languages list to a list of sets for easier manipulation
        lang_sets = [set() for _ in range(len(languages) + 1)]
        for i, langs in enumerate(languages):
            lang_sets[i + 1] = set(langs)
        
        # Identify users who need to learn a new language
        users_to_check = set()
        for u, v in friendships:
            if not (lang_sets[u] & lang_sets[v]):
                users_to_check.add(u)
                users_to_check.add(v)
        
        # Calculate the minimum number of users to teach for each language
        min_teachings = float('inf')
        for lang in range(1, n + 1):
            teachings_needed = sum(1 for user in users_to_check if lang not in lang_sets[user])
            min_teachings = min(min_teachings, teachings_needed)
        
        return min_teachings

def minimumTeachings(n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
    return Solution().minimumTeachings(n, languages, friendships)