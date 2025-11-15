import random
import functools
import collections
import string
import math
import datetime


from typing import List
from collections import deque, defaultdict

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        # BFS to find all friends at the given level
        def bfs(start_id, target_level):
            queue = deque([(start_id, 0)])  # (current_id, current_level)
            visited = set([start_id])
            level_friends = []
            
            while queue:
                current_id, current_level = queue.popleft()
                
                if current_level == target_level:
                    level_friends.append(current_id)
                    continue
                
                for friend in friends[current_id]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append((friend, current_level + 1))
            
            return level_friends
        
        # Get all friends at the specified level
        level_friends = bfs(id, level)
        
        # Count the frequency of each video watched by these friends
        video_count = defaultdict(int)
        for friend in level_friends:
            for video in watchedVideos[friend]:
                video_count[video] += 1
        
        # Sort videos first by frequency, then alphabetically
        sorted_videos = sorted(video_count.items(), key=lambda x: (x[1], x[0]))
        
        # Return only the video names
        return [video for video, count in sorted_videos]

def watchedVideosByFriends(watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    return Solution().watchedVideosByFriends(watchedVideos, friends, id, level)