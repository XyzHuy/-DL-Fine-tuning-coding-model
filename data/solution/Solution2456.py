import random
import functools
import collections
import string
import math
import datetime


from typing import List

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        from collections import defaultdict
        
        # Dictionary to store total views for each creator
        creator_views = defaultdict(int)
        # Dictionary to store the most viewed video for each creator
        creator_max_view = defaultdict(list)
        
        # Populate the dictionaries
        for i in range(len(creators)):
            creator = creators[i]
            video_id = ids[i]
            view_count = views[i]
            
            # Update total views for the creator
            creator_views[creator] += view_count
            
            # Update the most viewed video for the creator
            if creator not in creator_max_view or view_count > creator_max_view[creator][1] or (view_count == creator_max_view[creator][1] and video_id < creator_max_view[creator][0]):
                creator_max_view[creator] = [video_id, view_count]
        
        # Find the maximum popularity
        max_popularity = max(creator_views.values())
        
        # Collect all creators with the maximum popularity
        result = []
        for creator, total_views in creator_views.items():
            if total_views == max_popularity:
                result.append([creator, creator_max_view[creator][0]])
        
        return result

def mostPopularCreator(creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
    return Solution().mostPopularCreator(creators, ids, views)