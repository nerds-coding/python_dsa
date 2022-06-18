# https://www.interviewbit.com/technical-interview-questions/


def findMaxLength(nums):
    count = 0
    map = {0: -1}
    max_length = 0

    for i, number in enumerate(nums):
        if number:
            count += 1
        else:
            count -= 1

        if count in map:
            max_length = max(max_length, (i - map[count]))
        else:
            map[count] = i
        print(count)
    return max_length


print(findMaxLength([1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]))
