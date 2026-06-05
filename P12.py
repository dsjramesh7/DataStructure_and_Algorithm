#issue
from bisect import bisect_left

def lengthoOfLIS(nums):
    lis = []

    for num in nums:
        pos = bisect_left(lis, num)

        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num

    return len(lis)