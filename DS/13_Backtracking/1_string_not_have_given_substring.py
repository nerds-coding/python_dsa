from re import S


def safe_to_swap(st, cur_idx, swap_with):

    if swap_with - 1 != 0 and st[swap_with - 1] == "A" and st[cur_idx] == "B":
        return False

    return True


def string_not_have_given_substring(st, swap_with):

    if swap_with == len(st) - 1:
        print("".join(st))
        return

    for cur_idx in range(swap_with, len(st)):

        if safe_to_swap(st, cur_idx, swap_with):
            st[swap_with], st[cur_idx] = st[cur_idx], st[swap_with]

            string_not_have_given_substring(st, swap_with + 1)

            st[swap_with], st[cur_idx] = st[cur_idx], st[swap_with]


st = ["A", "B", "C"]

string_not_have_given_substring(st, 0)
