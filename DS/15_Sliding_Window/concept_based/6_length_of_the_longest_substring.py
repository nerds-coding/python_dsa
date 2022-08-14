# https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1

# catch and release technique


def longestUniqueSubsttr(s):
    ans = 1
    i = j = 0
    counter = set()
    n = len(s)
    while j < n:

        if s[j] not in counter:
            counter.add(s[j])
            ans = max(ans, len(counter))
        else:
            while counter and s[j] in counter:
                counter.remove(s[i])
                i += 1

            counter.add(s[j])

            ans = max(ans, len(counter))
        j += 1

    return ans
