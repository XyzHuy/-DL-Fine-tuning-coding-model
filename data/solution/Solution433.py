import random
import functools
import collections
import string
import math
import datetime


from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Convert bank to a set for faster lookup
        bank_set = set(bank)
        
        # Possible mutations at each position
        possible_mutations = {'A': 'CGT', 'C': 'AGT', 'G': 'ACT', 'T': 'ACG'}
        
        # Queue for BFS (gene, number of mutations)
        queue = deque([(startGene, 0)])
        
        # Set to keep track of visited genes
        visited = set([startGene])
        
        while queue:
            current_gene, mutations = queue.popleft()
            
            # If we have reached the end gene, return the number of mutations
            if current_gene == endGene:
                return mutations
            
            # Try to change each character in the current gene
            for i in range(len(current_gene)):
                for mutation in possible_mutations[current_gene[i]]:
                    next_gene = current_gene[:i] + mutation + current_gene[i+1:]
                    if next_gene in bank_set and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, mutations + 1))
        
        # If we exhaust the queue without finding the end gene, return -1
        return -1

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    return Solution().minMutation(startGene, endGene, bank)