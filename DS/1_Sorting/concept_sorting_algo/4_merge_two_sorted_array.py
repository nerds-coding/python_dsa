def merge_sorted_array(a, b):
    arr = []

    a_len = len(a)
    b_len = len(b)

    i = j = 0

    while i < a_len and j < b_len:

        if a[i] < b[j]:
            arr.append(a[i])
            i += 1
        else:
            arr.append(b[j])
            j += 1

    while i < a_len:
        arr.append(a[i])
        i += 1
    while j < b_len:
        arr.append(b[j])
        j += 1
    return arr


a = [2, 4, 6, 8]
b = [1, 3, 5, 7, 9]
print(merge_sorted_array(a, b))
