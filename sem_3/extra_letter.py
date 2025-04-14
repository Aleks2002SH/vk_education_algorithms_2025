
def hash_map(s):
    hash_tab = dict()
    for ch in s:
        if ch in hash_tab.keys():
            hash_tab[ch] += 1
        else:
            hash_tab[ch] = 1
    return hash_tab


def extra_letter(a,b):
    hash_map_a = hash_map(a)
    for ch in b:
        if ch in hash_map_a.keys():
            hash_map_a[ch]-=1
            if hash_map_a[ch]==0:
                del hash_map_a[ch]
        else:
            return ch
    return ""


