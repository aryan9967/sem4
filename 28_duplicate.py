l1 = [1, 2, 3, 4, 1, 6, 7, 9, 3, 4]
l2 =[]

def remove_dup(list1):
    seen = []
    
    for x in list1:
        if x not in seen:
            seen.append(x)
            
    return seen

print(remove_dup(l1))