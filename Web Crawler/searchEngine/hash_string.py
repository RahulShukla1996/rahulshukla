def hash_string(keyword,bucket):
    h = 0
    for c in keyword:
        h = (h + ord(c)) % bucket
    return h
print hash_string('a',12)
