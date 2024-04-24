s = {3, 5, 32, 3}
s2 = {4, 5, 6, 9}
print(s.union(s2))
print(s)
print(s.intersection(s2))
print(s.pop())

s.add(6)
s.remove(3)
print(s)

s3 ={5, 6, 9, 4, 5}
s3.discard(5)
print(s3)
s3.update(s2)
print(s3)
s4 = s3.copy()
print(s4)
print(s4.issubset(s3))
print(s4.issuperset(s3))
s4.clear()
print(s4)