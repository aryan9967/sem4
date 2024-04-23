'''Yes, an anagram of a string has the same number 
of characters as the original string, but the 
order of the characters can be different. 
For example, "abcd" and "dabc" are anagrams of each other. '''

a = input("enter first string: ")
b = input("enter second string: ")

flag = True

if(len(a) == len (b)):
    for x in a:
        if(b.index(x) == -1):
            flag = False
            break
        else:
            flag = True    
else:
    flag = False

if(flag):
    print("it is an anagram")
else:
    print("it is not an anagram")
        
