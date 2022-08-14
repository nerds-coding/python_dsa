def generate(numRows):
    arr = []
    if(numRows == 1):
        arr.append([1])
        return arr
    
    arr.append([1])
    if(numRows == 2):
        arr.append([1, 1])
        return arr
    arr.append([1, 1])

    count = 3

    for i in range(2, numRows):
        arr.append([1]*count)
        count += 1

        for j in range(1, len(arr[i])-1):
            arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
    return arr

print(generate(2))
