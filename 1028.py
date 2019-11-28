n = int(input())
name, date = [], []
for i in range(n):
    x = input().split()
    if x[1] <= '2014/09/06' and x[1] >= '1814/09/06':
        name.append(x[0])
        date.append(x[1])
if len(name) == 0:
    print("0")
else:
    print(len(date), name[date.index(min(date))], name[date.index(max(date))])
# 测试点4的数据量大，运行超时
