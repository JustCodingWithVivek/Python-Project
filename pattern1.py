n=int(input("Enter number of rows you want: "))
k = 1
for i in range(0, n):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()
