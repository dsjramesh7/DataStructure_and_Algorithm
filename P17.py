def largest(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num


print(largest([3, 7, 2, 9, 5])) 