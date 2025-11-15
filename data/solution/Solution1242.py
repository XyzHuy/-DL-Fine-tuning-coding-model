import random
import functools
import collections
import string
import math
import datetime


# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

import threading

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url):
            return url.split('/')[2]
        
        def worker():
            while True:
                url = queue.pop(0)
                if url not in visited:
                    visited.add(url)
                    for next_url in htmlParser.getUrls(url):
                        if get_hostname(next_url) == hostname and next_url not in visited:
                            queue.append(next_url)
                if len(queue) == 0:
                    break
        
        hostname = get_hostname(startUrl)
        visited = set()
        queue = [startUrl]
        
        num_threads = 8  # You can adjust the number of threads
        threads = []
        
        for _ in range(num_threads):
            thread = threading.Thread(target=worker)
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
        
        return list(visited)

def crawl(startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
    return Solution().crawl(startUrl, htmlParser)