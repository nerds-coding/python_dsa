def sortedSquares(nums):
    nums = list(map(lambda x: x*x, nums))

    ans = [0]*len(nums)
    ans[0] = nums[0]

    for i in range(1, len(nums)):
        high = len(ans)
        low = 0
        mid = 0
        while(low < high):
            mid = (low+high)//2

            if(ans[mid] == i):
                break
            elif(ans[mid] < i):
                high = mid
            else:
                low = mid

        if(ans[mid] == i):
            ans.insert(mid+1, i)
        elif(ans[mid] < i):
            ans.insert(mid+1, i)
        else:
            ans.insert(mid, i)
    return ans


print(sortedSquares([-4, -1, 0, 3, 10]))
