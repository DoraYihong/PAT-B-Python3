n, d = list(map(int, input().split()))
reserve = list(map(float, input().split()))  # 库存量不一定是整数
total_price = list(map(float, input().split()))  # 总售价不一定是整数
unit_price = {i: total_price[i] / reserve[i] for i in range(n)}
order = sorted(unit_price, key=lambda i: unit_price[i], reverse=True)
income = 0
for i in order:
    if reserve[i] < d:
        d -= reserve[i]
        income += total_price[i]
    else:
        income += unit_price[i] * d
        break
print('%.2f' % income)
