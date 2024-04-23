a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a<b and a<c):
    min = a
elif(b<c and b<a):
    min = b
else:
    min = c

print(min)