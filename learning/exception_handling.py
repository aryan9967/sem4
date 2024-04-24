try:
    a = int(input("enter number: "))
    print( a + 3)
except Exception as e:
    print("some error occured", e)