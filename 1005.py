num = int(input())
s = input()
x = s.split()

y = []
for n in x:
    y.append(int(n))
x = y

remo = []
for i in range(num):
    n = y[i]  # 注意把字符串转化为数字处理
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            if int(n) in x:
                remo.append(int(n))
        else:
            n = (3 * n + 1) / 2
            if int(n) in x:
                remo.append(int(n))
remo = list(set(remo))  # 去重
for i in range(len(remo)):
    x.remove(remo[i])
x.sort(reverse=True)  # 降序排序
for i in range(len(x) - 1):
    print(str(x[i]), end=" ")
print(x[len(x) - 1], end="")
