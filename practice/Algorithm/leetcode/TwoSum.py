

# two-pointer
def two_sum1(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]
        elif s < target:
            left += 1
        else:
            right -= 1


# dictionary
def two_sum2(numbers, target):
    dic = {}
    for i, num in enumerate(numbers, 1):
        if target - num in dic:
            return [dic[target - num], i]
        dic[num] = i


# binary search
def two_sum3(numbers, target):
    for i in range(len(numbers)):
        left, right = i + 1, len(numbers) - 1
        tmp = target - numbers[i]
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] == tmp:
                return [i + 1, mid + 1]
            elif numbers[mid] < tmp:
                left = mid + 1
            else:
                right = mid - 1