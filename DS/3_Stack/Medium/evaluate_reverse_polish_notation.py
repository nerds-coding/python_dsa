# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def operator(self, op, temp1, temp2):
        if op == "+":
            return temp1 + temp2
        elif op == "-":
            return temp2 - temp1
        elif op == "*":
            return temp1 * temp2
        elif op == "/":
            return int(temp2 / temp1)
        else:
            return False

    def evalRPN(self, tokens):
        stack = list()
        n = len(tokens)

        for i in range(0, n):
            print(stack)
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
            else:
                stack.append(
                    self.operator(
                        tokens[i], stack.pop(), stack.pop()
                        )
                    )

            # print(stack)

        return stack.pop()


sol = Solution()
print(sol.evalRPN(["4", "13", "5", "/", "+"]))
