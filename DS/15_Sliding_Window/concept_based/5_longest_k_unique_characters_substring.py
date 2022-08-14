# https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1


# catch and release technique

def longestKSubstr(self, s, k):
    ans = -1

    i = j = 0
    n = len(s)
    counter = dict()
    while j < n:

        counter[s[j]] = 1 + counter.get(s[j], 0)

        if len(counter) == k:
            ans = max(ans, j - i + 1)
        elif len(counter) > k:
            while len(counter) > k:
                if counter[s[i]] == 1:
                    counter.pop(s[i])
                else:
                    counter[s[i]] -= 1
                i += 1
        j += 1

    return ans

