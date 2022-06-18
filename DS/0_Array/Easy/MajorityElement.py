def majorityElement(nums):
    count = {}
    n = len(nums)
    for i in nums:
        count[i] = 0

    for i in range(0, n):
        count[nums[i]] += 1

    ans = 0
    temp = 0
    for key, values in count.items():
        if values > (n / 2) and (temp < values):
            ans = key
            temp = values

    return ans


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
