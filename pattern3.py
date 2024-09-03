# Number of rows for the pattern
n = 5

# Print the pattern from right to left
for i in range(1, n + 1):
    print(' ' * (n - i) * 2 + '* ' * i)

for i in range(n - 1, 0, -1):
    print(' ' * (n - i) * 2 + '* ' * i)
