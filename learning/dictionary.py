# a ={}
# b = set()
# print(a, type(a))
# print(b, type(b))

dict1= {
    "good" : "something pleasent",
    77 : "Aryan Maurya",
    76 : "Vamshi Marri"
}
dict2 = {
    76 : "Aryan Maurya",
    77 : "Vamshi Marri",
    44: "ayush"
}
print(dict1)
print(dict1[77])
print(dict1["good"])

dict1[72] = "Aniket"

print(dict1)

print(dict1.get(77))

print(dict1.values())
print(dict1.items())
print(dict1)
dict1.pop(77)
print(dict1)
dict1.update(dict2)
print(dict1)
dict3 = dict1.copy()
print(dict3)
print(dict2)
dict2.popitem()
print(dict2)
print(dict2.keys())
dict1.clear()
print(dict1)


# print(dict2.fromkeys(76))
x = dict2.setdefault(76 , "raj")
print(x)

print(dict2)