# # 1. Leaders in an Array 

# nums = [-3, 4, 5, 1, -4, -5]

# def leaders_in_array(nums):
#     n = len(nums)
#     if n == 0:
#         return []
    
#     leaders = []
#     max = nums[n - 1]

#     for i in range(n - 1, -1, -1):
#         if nums[i] >= max:
#             leaders.append(nums[i])
#             max = nums[i]
#     leaders.reverse()
#     return leaders
# print(leaders_in_array(nums))

# # 2. Reaarrange an array by signs
# nums = [1, 2, -3, -4, 5, -6]

# def rearrange_array_by_sign(nums):
#     pos = []
#     neg = []

#     for i in range(len(nums)):
#         if nums[i] < 0:
#             neg.append(nums[i])
#         else:
#             pos.append(nums[i])

#     result = []
#     for j in range(len(pos)):
#         result.append(pos[j])
#         result.append(neg[j])
#     return result
# print(rearrange_array_by_sign(nums))

# # 3. Count number of odd digits in a number
# n = 123456
# def count_odd_digits(n):
#     num = str(n)
#     cnt = 0
#     for num in num:
#         if int(num) % 2 != 0:
#             cnt += 1
#     return cnt
# print(count_odd_digits(n))

# 4. Union of two Sorted Arrays
arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

def union_of_sorted_arrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    i = 0
    j = 0

    result_arr = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            result_arr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            result_arr.append(arr2[j])
            j += 1
        else:
            result_arr.append(arr1[i])
            i += 1
            j += 1

    while i < n:
        result_arr.append(arr1[i])
        i += 1

    while j < m:
        result_arr.append(arr2[j])
        j += 1  

    return result_arr
print(union_of_sorted_arrays(arr1, arr2))