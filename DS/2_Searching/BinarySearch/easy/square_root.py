# https://leetcode.com/problems/sqrtx/


def mySqrt(x):
    low, high = 0, x

    mid, ans = 0, 0
    while low <= high:
        mid = low + (high - low) // 2

        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans


print(mySqrt(19))
