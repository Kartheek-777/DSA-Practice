# Majority Element-I

def majorityElement(nums):
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate

# Maximum Consecutive Ones

nums = [1, 1, 0, 1, 1, 1]
def finding_max_consecutive_Ones(nums):
    cnt = 0
    max_cnt = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            cnt += 1
            max_cnt = max(cnt, max_cnt)
        else:
            cnt = 0
    return max_cnt

#  Left Rotate an Array by one position

nums = [1, 2, 3, 4, 5]
def left_rotate_array(nums):
        n = len(nums)
        temp = nums[0]
        for i in range(1, n):
            nums[i-1] = nums[i]
        nums[n-1] = temp 

        return nums

# Left Rotate an Array by k positions

nums = [1, 2, 3, 4, 5]
def left_rotate_array_k(nums, k):
    n = len(nums)
    k = k % n
    elements = []
    Other_ele = []
    for i in range(k):
         elements.append(nums[i])
    for j in range(k, n):
        Other_ele.append(nums[j])

    ans = Other_ele + elements
    nums[:] = ans
    return nums

# 