rows  = int(input("Enter number of rows: "))
row_data = ""
for x in range(1, rows+1):
    for y in range(1, x+1):
        row_data = row_data + "*"
    print(row_data)
    row_data = ""