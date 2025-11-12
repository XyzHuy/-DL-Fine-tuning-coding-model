def reverseStr(s: str, k: int) -> str:
    N = len(s)
    ans = ""
    position = 0
    while position < N:
        nx = s[position : position + k]
        ans = ans + nx[::-1] + s[position + k : position + 2 * k]
        position += 2 * k
    return ans
