# https://www.interviewbit.com/blog/median-of-two-sorted-arrays/

def findMedianSortedArrays(arr1, arr2):
    len_a, len_b = len(arr1), len(arr2)

    if len_a > len_b:
        len_a, len_b = len_b, len_a

    total = len_a + len_b
    half = total // 2

    low, high = 0, len_a - 1

    while low <= high:

        mid = low + (high - low) // 2
        mid_half = half - mid - 2

        a_left = arr1[mid] if (mid >= 0) else float("-infinity")
        a_right = arr1[mid + 1] if (mid + 1 < len_a) else float("infinity")
        b_left = arr2[mid_half] if (mid_half >= 0) else float("-infinity")
        b_right = arr2[mid_half + 1] if (mid_half + 1 < len_b) else float("infinity")

        if a_left <= b_right and a_right >= b_left:
            if total % 2:
                return max(a_left, b_left) + min(b_right, a_right) / 2
            else:
                return max(b_right, a_right)
        elif a_left > b_right:
            high = mid - 1
        else:
            low = mid + 1
