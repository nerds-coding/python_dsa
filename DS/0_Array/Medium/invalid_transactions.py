# https://leetcode.com/problems/invalid-transactions/


def invalidTransactions(transactions):
    data = transactions.copy()
    n = len(transactions)
    ans = list()
    for i in range(0, n):
        data[i] = transactions[i].split(",")

    data = sorted(data)

    i = 1
    if int(data[0][2]) > 1000:
        ans.append(transactions[i])

    while i < n:
        if int(data[i][2]) > 1000:
            ans.append(transactions[i])
        elif int(data[i - 1][1]) + 60 >= int(data[i][1]) and (
            str(data[i - 1][0]) == str(data[i][0])
            and str(data[i - 1][3]) != str(data[i][3])
        ):
            ans.append(transactions[i])
            ans.append(transactions[i - 1])
        i += 1

    return list(set(ans))


print(invalidTransactions(transactions=["alice,20,800,mtv", "alice,50,100,beijing"]))
