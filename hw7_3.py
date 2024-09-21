x: int = int(input("Enter an odd number: "))
for i in range(1, x + 1, 2):
    for j in range(i, x):
        print(" ", end="")
    for j in range(1, i + 1):
        print(f"{j:^2}", end="")
    print()
for i in range(x + 1, 1, -2):
    for j in range(i - 2, x + 1):
        print(" ", end="")
    for j in range(1, i - 2):
        print(f"{j:^2}", end="")
    print()
