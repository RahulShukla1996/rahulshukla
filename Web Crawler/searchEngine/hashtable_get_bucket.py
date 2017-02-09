form hash_string import hash_string
def get_hash_table(hashtable,keyword):
    return hashtable[hash_string(keyword,len(hashtable))]
    
