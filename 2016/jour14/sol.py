# -*- coding: utf-8 -*- 
from hashlib import md5


def stretched_md5(s, times=1):
    h = md5(s.encode()).hexdigest()
    for _ in range(times-1):
        h = md5(h.encode()).hexdigest()
    return h

def first_repeat(s, n):
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
            if count == n:
                return s[i]
        else:
            count = 1
    return None

def solve(mot, stretch=1):
    keys = []
    hashes = []
    ind = 0

    def get_hash(i):
        if i >= len(hashes):
            hashes.append(stretched_md5(mot+str(i), stretch))
        return hashes[i]

    while len(keys) < 64:
        h = get_hash(ind)
        c = first_repeat(h, 3)
        if c:
            quint = c*5
            for j in range(ind+1, ind+1001):
                if quint in get_hash(j):
                    keys.append(ind)
                    break
        ind += 1

    return keys[63]

if __name__ == "__main__": 
    print("--- Jour 14 : Solution ---") 
    data = 'ngcjuoqr'
    data_test = 'abc'
    print("Attention l'execution est TRES Longue, environ 5 minutes . ")
    print("Test :", solve(data_test))   # devrait donner 22728
    print("Réel :", solve(data))
    print("Test 2 : ",solve(data_test,2017))
    print("Réel 2 : ", solve(data,2017))
