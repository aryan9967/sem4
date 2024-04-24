l1 = [1, 2, 4, 6, 8]
l2 = [4, 8, 9, 40, 20]

s1 = set(l1)
s2 = set(l2)

s3 = s1.union(s2)
s4 = s1.intersection(s2)

print(list(s3)), print(list(s4))