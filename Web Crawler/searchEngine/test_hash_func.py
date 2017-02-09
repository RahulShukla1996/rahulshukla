#from get_page import get_page
#from hash_string import hash_string

def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results        
#word = get_page('http://www.gutenburg.org/cache/epub/1661/pg1661.txt').split()
