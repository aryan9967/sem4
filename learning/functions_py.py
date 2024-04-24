def greethello(firstname, lastname):
    print(firstname, "inside greet hello", lastname)
    
greethello("Aryan", "Maurya")

def func2(fname, lname):
    st = f"hii my \n name is {fname} {lname}"
    print(st)
    
func2("Aryan", "Maurya")

def average(a, b):
    return (a+b)/2

x = average(4, 5)
print(x)