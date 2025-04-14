def create_array_of_anagramms(strs):
    def hash_func(s,mod = 10**9+7):
        alp_cnt = [0]*26
        for ch in s:
            alp_cnt[ord(ch)-ord('a')]+=1
        return tuple(alp_cnt)
    out_dict = dict()
    for s in strs:
        hash = hash_func(s)
        if hash not in out_dict.keys():
            out_dict[hash] = [s]
        else:
            out_dict[hash].append(s)
        
    return out_dict.values()