#lists are mutable
l1 = [5, 6, 7, 8, 9]

print(l1)
print(type(l1))

l2 = [5, 6, 7, 8, 9, "aryan"]
print(l2)
print(type(l2))

l2.remove("aryan")
l2.remove(9)
print(l2)
l2.sort()
l2.pop()
l2.append(1)
# l2.clear()
l2.extend(l1)
print(l2.count(8))
print(l2)
print(l2[0:4])

l1[0] = 'aryan'
print(l1)
l2.reverse()
l2.insert(0, "hii")
print(l2.index(5))
l1 = l2.copy()
print(l2)
print(l1)
l1.remove("hii")
print(l1)
print(l2)