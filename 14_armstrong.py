num = int(input("enter a number :"))
sum = 0
num_copy = num

while(num):
    digit = num % 10
    num = int(num/10)
    # print(num)
    sum = sum + digit*digit*digit
    # print("sum: ", sum)

#print(sum)    
if(num_copy == sum):
    print("it is an Armstrong number")
else:
    print("not an armstrong number")