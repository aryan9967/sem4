number = int(input("Enter a number"))

for i in range(1, 11):
    print(i*number)
    if(i == 3):
        break
    
a = [1, 23, 45, 67, 78]
s = {33, 33, 45, 67, 12}
for item in s:
    print(item)    
    
for i in range(10):
    if(i==3):
        continue
    print(i+1)    