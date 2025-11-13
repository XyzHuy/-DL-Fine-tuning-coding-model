def shortestDistance(words, word1, word2):
    index1 = index2 = -1
    res = len(words)
    for index, word in enumerate(words):
        if word1 == word:
            index1 = index
        elif word2 == word:
            index2 = index
        if index1 != -1 and index2 != -1:
            res = min(res, abs(index1 - index2))
    return res
