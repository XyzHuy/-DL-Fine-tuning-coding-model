def hIndex(citations):
    # counting sort
    ls = len(citations)
    papers = [0] * (ls + 1)
    for c in citations:
        papers[min(ls, c)] += 1
    k, s = ls, papers[ls]
    while k > s:
        k -= 1
        s += papers[k]
    return k
