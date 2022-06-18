# https://leetcode.com/problems/powx-n/


def myPow(x: float, n: int) -> float:
    ans = 1.0
    flag = False

    if n == 0:
        return 1
    elif n < 0:
        n *= -1
        flag = True

    while n > 0:
        if n % 2 != 0:
            ans *= x
            n -= 1
        x *= x
        n /= 2

    return ans if (not flag) else 1 / ans


print(myPow(2,10))