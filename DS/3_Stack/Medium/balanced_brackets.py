# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/


class Solution:
    def isValid(self, arr: str) -> bool:
        n = len(arr)
        stack = list()
        
        if(n == 1):
            return False
        closing = [")", "]", "}"]
        pairs = ["()", "[]", "{}"]

        for i in range(0, n):
            if arr[i] not in closing:
                stack.append(arr[i])
            else:
                if(stack):
                    if (stack and stack.pop() + arr[i] not in pairs):
                        return False
                else:
                    return False
                
        return stack == []


sol = Solution()
print(sol.isValid())
