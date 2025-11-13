def groupAnagrams(strs):
    strs.sort()
    hash = {}
    for s in strs:
        key = hash_key(s)
        try:
            hash[key].append(s)
        except KeyError:
            hash[key] = [s]
    return hash.values()

def hash_key( s):
    # hash string with 26 length array
    table = [0] * 26
    for ch in s:
        index = ord(ch) - ord('a')
        table[index] += 1
    return str(table)