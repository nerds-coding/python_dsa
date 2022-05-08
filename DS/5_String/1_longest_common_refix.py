# https://leetcode.com/problems/longest-common-prefix/


def longestCommonPrefix(strs):
    # sorting the list in ascending lenght order, 
    # so we can have the smallest first
    # reason to have smallest first is b'coz
    # we can't go beyond the smallest size for the prefix,
    # in any longer size string
    # because it will not make common/continous prefix
    strs.sort(key=len)

    # as we only have to find till the smallest string length
    # we will loop every string till the smallest string length
    search_l = len(strs[0])
    frst_word = strs[0]

    for i in range(1, len(strs)):  # we have already taken the first value
        for j in range(search_l):
            if frst_word[j] != strs[i][j]:
                # if we find any char not matching in any string
                # we will update the smallest string length
                # so we optimize the algo
                search_l = j
                break

    # check if common string exists or not
    # if exists then from the first string send till the optimized length
    return frst_word[:search_l] if search_l else ""


print(longestCommonPrefix(strs=["dog", "racecar", "car"]))
