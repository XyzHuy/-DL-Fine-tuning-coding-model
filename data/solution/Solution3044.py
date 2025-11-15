import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import defaultdict

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        directions = [
            (0, 1), (1, 1), (1, 0), (1, -1), 
            (0, -1), (-1, -1), (-1, 0), (-1, 1)
        ]
        m, n = len(mat), len(mat[0])
        prime_count = defaultdict(int)
        
        def traverse(x, y, dx, dy, current_number):
            nonlocal prime_count
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                current_number = current_number * 10 + mat[nx][ny]
                if current_number > 10 and is_prime(current_number):
                    prime_count[current_number] += 1
                traverse(nx, ny, dx, dy, current_number)
        
        for i in range(m):
            for j in range(n):
                for dx, dy in directions:
                    traverse(i, j, dx, dy, mat[i][j])
        
        if not prime_count:
            return -1
        
        # Find the most frequent prime number, and in case of a tie, the largest one
        most_frequent_prime = max(prime_count, key=lambda x: (prime_count[x], x))
        return most_frequent_prime

def mostFrequentPrime(mat: List[List[int]]) -> int:
    return Solution().mostFrequentPrime(mat)