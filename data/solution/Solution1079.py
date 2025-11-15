import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(path, tiles):
            if path:
                self.count += 1
            for i in range(len(tiles)):
                if i > 0 and tiles[i] == tiles[i - 1]:
                    continue
                backtrack(path + tiles[i], tiles[:i] + tiles[i+1:])
        
        self.count = 0
        tiles = sorted(tiles)
        backtrack("", tiles)
        return self.count

def numTilePossibilities(tiles: str) -> int:
    return Solution().numTilePossibilities(tiles)