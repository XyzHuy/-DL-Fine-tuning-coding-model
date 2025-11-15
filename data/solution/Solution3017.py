import random
import functools
import collections
import string
import math
import datetime


from collections import defaultdict

class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> list[int]:
        if x > y:
            x, y = y, x
        
        def count_pairs_with_shortest_path(n, x, y):
            result = [0] * n
            for i in range(1, n + 1):
                distances = defaultdict(lambda: float('inf'))
                distances[i] = 0
                queue = [(i, 0)]
                
                while queue:
                    current, dist = queue.pop(0)
                    if dist > 0:
                        result[dist - 1] += 1
                    
                    # Move to the next house in the line
                    if current < n and distances[current + 1] == float('inf'):
                        distances[current + 1] = dist + 1
                        queue.append((current + 1, dist + 1))
                    
                    # Move to the previous house in the line
                    if current > 1 and distances[current - 1] == float('inf'):
                        distances[current - 1] = dist + 1
                        queue.append((current - 1, dist + 1))
                    
                    # Use the special edge from x to y
                    if current == x and distances[y] == float('inf'):
                        distances[y] = dist + 1
                        queue.append((y, dist + 1))
                    
                    # Use the special edge from y to x
                    if current == y and distances[x] == float('inf'):
                        distances[x] = dist + 1
                        queue.append((x, dist + 1))
            
            return result
        
        return count_pairs_with_shortest_path(n, x, y)

# Example usage:
# sol = Solution()
# print(sol.countOfPairs(3, 1, 3))  # Output: [6, 0, 0]
# print(sol.countOfPairs(5, 2, 4))  # Output: [10, 8, 2, 0, 0]
# print(sol.countOfPairs(4, 1, 1))  # Output: [6, 4, 2, 0]

def countOfPairs(n: int, x: int, y: int) -> list[int]:
    return Solution().countOfPairs(n, x, y)