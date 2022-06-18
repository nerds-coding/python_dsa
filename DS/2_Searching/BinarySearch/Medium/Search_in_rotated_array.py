class Solution:
    def binary_search(self, arr, target):
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def search(self, arr, target):

        low, high, ans = 0, len(arr) - 1, -1
        n = high + 1

        if n == 1:
            return 0 if (arr[0] == target) else -1
        elif arr[0] < arr[n - 1]:
            return self.binary_search(arr, target)
        else:
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] < arr[mid - 1] and arr[mid] < arr[mid + 1]:
                    ans = mid
                    break
                elif arr[mid] < arr[high]:
                    high = mid - 1
                else:
                    low = mid + 1

            if arr[0] > target and arr[ans - 1] > target:
                j = self.binary_search(arr[ans:], target)
                return ans + j if (j >= 0) else j
            else:
                return self.binary_search(arr[:ans], target)


sol = Solution()

arr = [4, 5, 6, 7, 0, 1, 2]
print(sol.search(arr, 7))
