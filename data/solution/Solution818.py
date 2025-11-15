import random
import functools
import collections
import string
import math
import datetime


class Solution:
    def racecar(self, target: int) -> int:
        from collections import deque
        
        # (position, speed)
        queue = deque([(0, 1)])
        visited = set((0, 1))
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                pos, speed = queue.popleft()
                
                # If we reach the target, return the number of steps
                if pos == target:
                    return steps
                
                # Accelerate: 'A'
                new_pos = pos + speed
                new_speed = speed * 2
                if (new_pos, new_speed) not in visited and 0 < new_pos < 2 * target:
                    visited.add((new_pos, new_speed))
                    queue.append((new_pos, new_speed))
                
                # Reverse: 'R'
                new_speed = -1 if speed > 0 else 1
                if (pos, new_speed) not in visited:
                    visited.add((pos, new_speed))
                    queue.append((pos, new_speed))
            
            # Increment the step count after exploring all nodes at the current level
            steps += 1

def racecar(target: int) -> int:
    return Solution().racecar(target)