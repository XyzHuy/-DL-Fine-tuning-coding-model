import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        # Define the maximum bit length for the numbers
        MAX_BITS = 15  # Since 2 * 10^4 < 2^15
        
        # Trie node class
        class TrieNode:
            def __init__(self):
                self.children = [None, None]  # 0 and 1
                self.count = 0
        
        # Trie root
        root = TrieNode()
        
        # Function to insert a number into the Trie
        def insert(num):
            node = root
            for i in range(MAX_BITS, -1, -1):
                bit = (num >> i) & 1
                if node.children[bit] is None:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
                node.count += 1
        
        # Function to count numbers in the Trie that have XOR with num < val
        def countLessThan(num, val):
            node = root
            count = 0
            for i in range(MAX_BITS, -1, -1):
                if node is None:
                    break
                bit = (num >> i) & 1
                val_bit = (val >> i) & 1
                if val_bit == 1:
                    if node.children[bit] is not None:
                        count += node.children[bit].count
                    node = node.children[1 - bit]
                else:
                    node = node.children[bit]
            return count
        
        # Main logic
        nice_pairs_count = 0
        for num in nums:
            # Count numbers that have XOR with num in [low, high]
            nice_pairs_count += countLessThan(num, high + 1) - countLessThan(num, low)
            # Insert the current number into the Trie
            insert(num)
        
        return nice_pairs_count

def countPairs(nums: List[int], low: int, high: int) -> int:
    return Solution().countPairs(nums, low, high)