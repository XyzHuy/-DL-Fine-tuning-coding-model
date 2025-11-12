
solution = {}

def wordBreak(s, wordDict):
    global solution
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    try:
        return solution[s]
    except KeyError:
        pass
    result = []
    if s in wordDict:
        result.append(s)
    for i in range(1, len(s)):
        word = s[i:]
        if word in wordDict:
            rem = s[:i]
            prev = wordBreak(rem, wordDict)
            result.extend([res + ' ' + word for res in prev])
    solution[s] = result
    return result