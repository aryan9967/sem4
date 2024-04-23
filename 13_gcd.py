import math

# print(math.gcd(12 , 24))

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))



if(num1>num2):
    final_limit = num2
else:
    final_limit = num1
         
i = 1
while (i <= final_limit):
    if(num1 % i == 0 and num2 % i == 0):
        gcd = i
    i += 1
print(gcd)