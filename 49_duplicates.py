result = {}
dict1 = {'a':5, 'b': 6, 'c': 7, 'd': 2, 'a':5, 'b': 6, 'c': 7, 'd': 2 }
for x,y in dict1.items():
    if x not in result.keys():
        result[x] = y
print(result)