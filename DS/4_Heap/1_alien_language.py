# https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203175/Python-straightforward-solution


def isAlienSorted(words, order):
    ind = {c: i for i, c in enumerate(order)}
    for a, b in zip(words, words[1:]):
        if len(a) > len(b) and a[: len(b)] == b:
            return False
        for s1, s2 in zip(a, b):
            if ind[s1] < ind[s2]:
                break
            elif ind[s1] > ind[s2]:
                return False
    return True


print(isAlienSorted(["hello", "hello"], "abcdefghijklmnopqrstuvwxyz"))
