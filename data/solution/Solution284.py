def licenseKeyFormatting(S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """
    S = S.upper().replace('-', '')
    ls = len(S)
    if ls % K == 0:
        pos = K
    else:
        pos = ls % K
    res = S[:pos]
    while pos < ls:
        res += '-' + S[pos:pos + K]
        pos += K
    return res
