def permutation(st, swap_idx):

    if swap_idx == len(st) - 1:
        print("".join(st))

    for swap_with in range(swap_idx, len(st)):
        st[swap_with], st[swap_idx] = st[swap_idx], st[swap_with]

        permutation(st, swap_idx + 1)

        st[swap_with], st[swap_idx] = st[swap_idx], st[swap_with]


st = ["A", "B", "C"]

# permutation(st, 0)


def is_safe(left, right, cur):

    if len(right) > 0 and cur + right[0] == "AB":
        return False

    if len(left) > 0 and cur + left[0] == "AB":
        return False

    return True


def string_permutation(given_str, ans):

    if len(given_str) == 0:
        print("".join(ans))
        return

    for i in range(len(given_str)):

        fixed_str = given_str[i]

        left_side = given_str[:i]
        right_side = given_str[i + 1:]

        new_str = left_side + right_side

        if is_safe(left_side, right_side, fixed_str):
            string_permutation(new_str, ans + fixed_str)
        # print(f"{i}  {ans}")


string_permutation(st, "")
