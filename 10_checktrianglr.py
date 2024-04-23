side1 = int(input("Enter length of firstside : "))
side2 = int(input("Enter length of secondside : "))
side3 = int(input("Enter length of thirdside : "))

if(side1 == side2 and side1 == side3):
    print("equilateral triangle")
elif(side1 == side2 or side2 == side3 or side1 == side3):
    print("isosceles triangle")
else:
    print("scalene triangle")