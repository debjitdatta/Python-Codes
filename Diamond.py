# Reading number of row
row = int(input('Enter number of row: '))

# Upper half
for x in range(1, row+1):
    for y in range(1,row-x+1):
        print(" ", end="")
    for y in range(1, 2*x):
        print("*", end="")
    print()

# Lower half
for x in range(row-1,0, -1):
    for y in range(1,row-x+1):
        print(" ", end="")
    for y in range(1, 2*x):
        print("*", end="")
    print()