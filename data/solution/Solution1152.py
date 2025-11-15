import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict
from itertools import combinations
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Combine and sort the data by timestamp
        combined = sorted(zip(timestamp, username, website))
        
        # Create a dictionary to hold the websites visited by each user in order
        user_sites = defaultdict(list)
        for _, user, site in combined:
            user_sites[user].append(site)
        
        # Dictionary to count the occurrences of each 3-sequence
        pattern_count = defaultdict(set)
        
        # Generate all 3-sequences for each user and count them
        for user, sites in user_sites.items():
            for seq in combinations(sites, 3):
                pattern_count[seq].add(user)
        
        # Find the sequence with the maximum number of users
        max_count = max(len(users) for users in pattern_count.values())
        
        # Filter the sequences with the maximum count and return the lexicographically smallest one
        best_patterns = [seq for seq, users in pattern_count.items() if len(users) == max_count]
        return min(best_patterns)

def mostVisitedPattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    return Solution().mostVisitedPattern(username, timestamp, website)