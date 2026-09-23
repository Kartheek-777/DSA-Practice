# Remove duplicates from sorted array

def remove_duplicates(nums):
    if nums == 0:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1

# First Occurrence of element in sorted array

def First_Occurrence(nums, target):
    n = len(nums)
    for i in range(n):
        if nums[i] == target:
            return i 
    return -1

# Second Occurrence of element in sorted array

def Second_Occurrence(nums, target):
    cnt = 0
    for i in range(len(nums)):
        if nums[i] == target:
            cnt += 1
            if cnt == 2:
                return i
    return -1

# Armstrong Number

n = int(input("Enter a number: "))
def armstrong_number(n):
    num = n
    total = 0
    length = len(str(n))
    while n > 0:
        digit = n % 10
        total += digit ** length
        n //= 10
    return total == num
if armstrong_number(n):
    print(f"{n} is an Armstrong Number")
else:
    print(f"{n} is not an Armstrong Number")

# GCD of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a 
print(f"GCD of {a} and {b} is :", gcd(a, b))

# Prime Number

n = int(input("Enter a number: "))
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
if is_prime(n):
   print(f"{n} is a Prime Number") 
else:
    print(f"{n} is not a Prime Number")

# Factorial of a number

n  = int(input("Enter a number: "))
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Factorial of {n} is :", factorial(n))

# Binary Search

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Target = int(input("Enter a number to search: "))
def binary_search(nums, target):
    left = nums[0]
    right = nums[-1]

    for i in range(len(nums)):
        mid  = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print("Index of Target", {Target}," is :", binary_search(nums, Target))
