def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    res = ord(t[-1])
    for i in range(len(s)):
        res += ord(t[i])
        res -= ord(s[i])
    return chr(res)
