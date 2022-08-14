def search(pat, txt):

    s_count = {}  # given txt
    p_count = {}  # pattern

    ans = 0

    for i in range(len(pat)):
        s_count[txt[i]] = 1 + s_count.get(txt[i], 0)
        p_count[pat[i]] = 1 + p_count.get(pat[i], 0)

    if s_count == p_count:
        ans += 1

    l = 0  # to keep account of winodws size or
    # remove the previous value from windows
    for i in range(len(pat), len(txt)):
        s_count[txt[i]] = 1 + s_count.get(txt[i], 0)
        s_count[txt[l]] -= 1

        # this will check if the value == 0
        # it means that, value of txt is now of index

        # if greater then 0 it means there is repeating value in the
        # txt so we cannot pop it from the dict()
        if s_count[txt[l]] == 0:
            s_count.pop(txt[l])
        l += 1

        if s_count == p_count:
            ans += 1

    return ans
