a = int(input("enter a number: "))

match a:
    case 1:
        print("case is 1")
    case 2:
        print("case is 2")
    case 3:
        print("case is 3")
    case _: 
        print("default")
        