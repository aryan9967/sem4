st = input("Enter a string :")
i = 0

flag = True
for i in range(len(st)):
    if(st[i] != st[len(st) - 1 - i]):
        flag = False
        break;    
    
if(flag == False):
    print("it is not a pallindrome")

else:
    print("it is a pallindrome")