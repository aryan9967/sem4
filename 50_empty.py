dict1 = {'a':5, 'b': 6, 'c': 7, 'd': 2, 'a':5, 'b': 6, 'c': 7, 'd': 2 }
dict2 = {}
print()

def empty_check(dict1):
    return bool(dict1)

print(empty_check(dict1))
print(empty_check(dict2))