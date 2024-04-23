colors = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))

flag = False
for x in colors:
    for y in x:
        if(y == "White"):
            flag = True
            break

print(flag)