# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/


# answer description
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/661995/Do-you-like-visual-explanation-You-got-it.-%3A-)-With-2-code-variations.


def maxArea(h, w, horizontalCuts, verticalCuts):
    h_cuts = [0] + sorted(horizontalCuts) + [h]
    v_cuts = [0] + sorted(verticalCuts) + [w]

    maxStripWidth = max(
        [h_cuts[i + 1] - h_cuts[i] for i in range(len(h_cuts) - 1)])
    maxStripHeight = max(
        [v_cuts[i + 1] - v_cuts[i] for i in range(len(v_cuts) - 1)])

    return (maxStripWidth * maxStripHeight) % ((10**9) + 7)


print(maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))
