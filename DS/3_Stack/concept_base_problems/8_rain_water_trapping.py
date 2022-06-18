def rain_water_trapping(arr):
    n = len(arr)
    pre_max = [0] * n
    pre_max[0] = arr[0]

    suffix_max = [0] * n
    suffix_max[-1] = arr[-1]

    for i in range(1, n):
        if pre_max[i - 1] < arr[i]:
            pre_max[i] = arr[i]
        else:
            pre_max[i] = pre_max[i - 1]

        if suffix_max[n - i] < arr[n - i - 1]:
            suffix_max[n - i - 1] = arr[n - i - 1]
        else:
            suffix_max[n - i - 1] = suffix_max[n - i]

    sum_rain = 0

    for i in range(0, n):
        sum_rain += min(pre_max[i], suffix_max[i]) - arr[i]

    return sum_rain


print(rain_water_trapping([3, 0, 2, 0, 4]))
