k = 0
for x in range(452022, 1000000):
    a = []
    for delit in range(2,x):
        if x % delit == 0:
            a.append(delit)
            if len(a) >= 2:
                M = a[0] + a[-1]
            else:
                M = 0
    if M % 7 == 3:
        k += 1
        print(x , M)
    if k == 5:
        break