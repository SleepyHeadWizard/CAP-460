print("\nPattern 6\n")
n=5
for i in range(n, 0, -1):
    print("*" * i, end="")
    print(" " * (2 * (n - i) + 1), end="")
    print("*" * i)