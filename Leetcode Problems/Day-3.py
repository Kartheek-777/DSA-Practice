# # Reverse an array of integers in place.

arr = [1, 2, 3, 4, 5]
n = len(arr)
def Reverse_array(arr):
    if n == 0:
        return arr
    for x in range(n // 2):
        arr[x], arr[n-x-1] = arr[n-x-1], arr[x]
    return arr
print(Reverse_array(arr))

# # Same Using two pointer approach

def reverse_array_two_pointer(arr):
    left = 0
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
print(reverse_array_two_pointer(arr))

# Check is a number is a palindrome or not

num = input("Enter a number: ")
n = len(str(num))
def is_palindrome(num):
    for i in range(n // 2):
        if num[i] != num[n-i-1]:
            return "Not a palindrome"
    return "Is a palindrome"
print(is_palindrome(num))

# Sum an array of integers without using sum() function

arr = [1, 2, 3, 4, 5]
def sum_array(arr):
    count = 0
    for i in range(len(arr)):
        count += arr[i]
    return count
print(sum_array(arr))

# Count of Odd numbers in an array

arr = [1, 2, 3, 7, 5]
n = len(arr)
def count_odd_numbers(arr, n):
    cnt = 0 
    for i in range(n):
        if arr[i] % 2 != 0:
            cnt += 1
    return cnt
print(count_odd_numbers(arr, n))

# Check Array is sorted or not

arr = [7, 2, 3, 4, 5]
def is_sorted(arr):
    for i in range(len(arr)-1):
          if arr[i] > arr[i+1]:
              return "Array is not sorted"
    return "Array is sorted"
print(is_sorted(arr))

# Reverse a number without converting it to string

num = 12345
def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev
print(reverse_number(num))

# Find the maximum and minimum element in an array

arr = [1, 2, 3, 4, 5]
def find_max_min(arr):
    max_num = arr[0]
    min_num = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
        if arr[i] < min_num:
            min_num = arr[i]
    return max_num, min_num
print(find_max_min(arr))
