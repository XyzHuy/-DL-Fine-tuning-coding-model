import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        
        # Calculate forces due to 'R'
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] += force
        
        # Calculate forces due to 'L'
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force
        
        # Determine final state
        result = []
        for force in forces:
            if force > 0:
                result.append('R')
            elif force < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)

def pushDominoes(dominoes: str) -> str:
    return Solution().pushDominoes(dominoes)