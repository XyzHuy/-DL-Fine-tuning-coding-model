def validWordSquare(words):
    """
    :type words: List[str]
    :rtype: bool
    """
    if words is None or len(words) == 0:
        return True
    ls = len(words)
    for i in range(ls):
        for j in range(1, len(words[i])):
            if j >= ls:
                return False
            if i >= len(words[j]):
                return False
            if words[i][j] != words[j][i]:
                return False
    return True
