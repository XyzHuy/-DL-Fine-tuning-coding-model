
def findLadders(beginWord, endWord, wordlist):
    # do not use single dfs or bfs, because both of them
    # try to get result in single direction, which check lots
    # of unnecessary branches
    wordlist.discard(beginWord)
    wordlist.discard(endWord)
    hash_map, res = {}, []
    bfs(set([beginWord]), set([endWord]), wordlist, False, hash_map)
    dfs(res, [beginWord], beginWord, endWord, hash_map)
    return res

def bfs(forward, backward, wordlist, reverse, hash_map):
    import string
    if len(forward) == 0 or len(backward) == 0:
        return
    if len(forward) > len(backward):
        bfs(backward, forward, wordlist, not reverse, hash_map)
        return
    is_connected = False
    next_level = set()
    for word in forward:
        for c in string.ascii_lowercase:
            for index in range(len(word)):
                neigh = word[:index] + c + word[index + 1:]
                if not reverse:
                    key, value = word, neigh
                else:
                    key, value = neigh, word
                if neigh in backward:
                    hash_map[key] = hash_map.get(key, []) + [value]
                    is_connected = True
                if not is_connected and neigh in wordlist:
                    next_level.add(neigh)
                    hash_map[key] = hash_map.get(key, []) + [value]
                    wordlist.discard(neigh)

    if not is_connected:
        bfs(next_level, backward, wordlist, reverse, hash_map)

def dfs(res, path, begin, end, hash_map):
    if begin == end:
        res.append(path)
        return
    try:
        next_step = hash_map[begin]
        for word in next_step:
            dfs(res, path + [word], word, end, hash_map)
    except KeyError:
        pass