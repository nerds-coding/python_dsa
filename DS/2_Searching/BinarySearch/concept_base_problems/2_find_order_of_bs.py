# here we have to find order of binary search
# such that it is
# Ascending or Descending


def order_finding(arr):
    if arr[0] < arr[-1]:
        return "Ascending Order"  # TODO then call the ascending BS
    else:
        return "Descending Order"  # TODO then call the Descending BS
