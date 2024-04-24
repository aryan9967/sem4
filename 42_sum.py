def sumofvalues(dictionary):
    sum = 0
    for x in dictionary.values():
        sum =sum + x
    return sum

dict1 = {'a':5, 'b': 6, 'c': 7, 'd': 2}
final_sum = sumofvalues(dict1)
print(final_sum)