class Solution:
    def is_valid(self, new_cur, snake):

        # checking the current value is in range of 1 to till 30
        # and that value is not present in snake dict()
        if new_cur >= 1 and new_cur <= 30 and new_cur not in snake:
            return True
        return False

    def minThrow(self, N, arr):

        # seperating the ladder pair and snaker pair
        # for simple calc
        ladder = dict()
        snake = dict()

        for i in range(0, len(arr), 2):
            if arr[i] < arr[i + 1]:
                ladder[arr[i]] = arr[i + 1]
            else:
                snake[arr[i]] = arr[i + 1]

        q = list()
        steps = 0

        # same logic as rotten Oranges
        # if the new step is valid the put in q for finding
        # any new possible optimized steps
        # if found in middle the return the steps +1
        q.append(1)
        while q:
            size = len(q)

            while size:

                cur = q.pop(0)
                # 1 , 7 bcz a dice have 1 to 6 vals only
                for i in range(1, 7):
                    new_cur = cur + i
                    # checking every possible dice with cur val

                    if new_cur == 30:
                        return steps + 1
                    if self.is_valid(new_cur, snake):
                        if new_cur in ladder:
                            q.append(ladder[new_cur])
                        else:
                            q.append(new_cur)
                size -= 1

            steps += 1

        return steps
