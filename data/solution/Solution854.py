import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        from collections import deque
        
        # Helper function to generate all strings possible by swapping one pair of characters
        def get_neighbors(s):
            neighbors = []
            i = 0
            # Find the first position where s1 and s2 differ
            while i < len(s) and s[i] == s2[i]:
                i += 1
            # Try swapping the differing character with any subsequent character that matches s2[i]
            for j in range(i + 1, len(s)):
                if s[j] == s2[i] and s[j] != s2[j]:
                    # Swap and generate a new string
                    new_s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                    neighbors.append(new_s)
            return neighbors
        
        # BFS to find the shortest path (minimum swaps)
        queue = deque([(s1, 0)])  # (current string, current swaps count)
        visited = set([s1])
        
        while queue:
            current, swaps = queue.popleft()
            
            # If we have reached the target string, return the number of swaps
            if current == s2:
                return swaps
            
            # Generate all possible strings by swapping one pair of characters
            for neighbor in get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, swaps + 1))

def kSimilarity(s1: str, s2: str) -> int:
    return Solution().kSimilarity(s1, s2)