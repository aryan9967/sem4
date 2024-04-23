x = [(1, 2), (2, 3), (3, 4)]
b = []
for y in x:
    sum = 0
    for inner in y:
        sum = sum + inner
    b.append(sum)
    
print(b)

l2 = [3, 5, 7]
# l3 = []
sum = 0
for y in l2:
    
    sum += y
    
print(sum)