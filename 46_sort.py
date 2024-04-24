dict1 = {'a':5, 'b': 6, 'c': 7, 'd': 2}

dict2 = dict(sorted(dict1.items()))
dict3 = dict(sorted(dict1.items(), reverse=True))
print(dict2, dict3)