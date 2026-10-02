col = int(input("cols? "))
row = int(input("rows? "))
print("* " * col)
for i in range(row-2):
    print("* " + "  " * (col-2) + "* ")
print("* " * col)