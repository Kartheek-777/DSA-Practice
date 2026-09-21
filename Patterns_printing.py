# 1. Normal Pattern

n = int(input("Enter the Value of n:"))
for i in range(1, n):
    for j in range(1, n):
        print("*", end=" ")
    print()

# 2.Increasing star Pattern

n = int(input("Enter the Value of n:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# 3. Increasing number Pattern

n = int(input("Enter the Value of n:"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")

    print()

# 4. Continuous number Pattern

n = int(input("Enter the Value of n:"))
num = 1 
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 5. Alphabet Pattern

n = int(input("Enter the Value of n:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    print()

# 6. Increasing Alphabet Pattern

n = int(input("Enter the Value of n:"))
num = 1
for i in range(1, n + 1):
    for j in range(1, i+1):
        print(chr(64 + num), end=" ")
        num += 1
    print()

# 7. Decreasing Star Pattern

n = int(input("Enter the Value of n:"))
for i in range(1, n+1):
    for j in range(n-i+1):
        print("*", end=" ")
    print()

# 8. Inverted Number Pattern

n = int(input("Enter the Value of n:"))
for i in range(1, n+1):
    for j in range(n-i+1):
        print(j+1, end=" ")
    print()

# 9. Inverted Increasing Number Pattern

n = int(input("Enter the Value of n:"))
num = 1
for i in range(1, n+1):
    for j in range(n-i+1):
        print(num, end = " ")
        num += 1

    print()

# 10. Inverted Alphabet Pattern

n = int(input("Enter the Value of n:"))

for i in range(1, n + 1):
    for j in range(n-i+1):
        print(chr(64 + j + 1), end=" ")
    print()

# 11. Inverted Increasing Alphabet Pattern

n = int(input("Enter the Value of n:"))
num = 0
for i in range(1, n + 1):
    for j in range(n-i+1):
        print(chr(64 + num + 1), end=" ")
        num += 1
    print()

# 12. Pyramid Pattern

n = int(input("Enter the Value of n:"))
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(1, i):
        print("*", end=" ")
    print()

# 13. Inverted Pyramid Pattern

n = int(input("Enter the Value of n:"))

for i in range(1, n + 1):
    for j in range(1, i):
        print(" ", end=" ")
    for j in range(n - i + 1):
        print("*", end=" ")
    for j in range(n - i):
        print("*", end=" ")
    print()
