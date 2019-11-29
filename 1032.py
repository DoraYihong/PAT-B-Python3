n = int(input())
sn = []
score = []
for i in range(n):
    sn0, score0 = list(map(int, input().split()))
    sn.append(sn0)
    score.append(score0)
sum_school = max(sn)
dic = {}
for i in range(n):
    try:
        dic[sn[i]] += score[i]
    except KeyError:
        dic[sn[i]] = score[i]
temp = max(dic, key=dic.get)
print(temp, dic[temp])
# 最后一个测试点超时
