a = int(input("enter a number: "))
sum = 0
def find_sum(num, sum):
    if num == 0:
        return sum
    else:
        return find_sum(num - 1, sum + num)

x = find_sum(a, sum)
print(x)
