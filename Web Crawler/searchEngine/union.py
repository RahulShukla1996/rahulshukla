l1 = [1,2,3]
l2 = [4,5,6]
def union(p, q):
    for i in q:
        if i not in p:
            p.append(i)
    return p, q
a, b = union(l1, l2)
print a, b
