from itertools import permutations

def find_permutations(lst):
    print(lst)
    perm_lst = permutations(lst)
    perm_lst = list(perm_lst)
    return perm_lst 

lst = [1, 2, 3, 4, 5, 6]
permutation_lst = find_permutations(lst)
print(permutation_lst)
    