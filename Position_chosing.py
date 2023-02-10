

row1 = ["😀","😃","😄"]
row2 = ["😁","😆","😅"]
row3 = ["🤣","🙂","😉"]

J = [row1,row2,row3]




x = int(input("row : "))- 1
y = int(input("line : ")) - 1

J[x][y] = "X"


SC = f"{row1}\n{row2}\n{row3}\n"

print(SC)

