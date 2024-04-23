for i in range(100, 401):
    flag = True
    copy = i
    while i:
        digit = i%10
        i = int(i/10)
        if(digit % 2 != 0):
            flag = False
            break
    if(flag == True):
        print(copy)