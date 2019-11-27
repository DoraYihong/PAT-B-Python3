s = input().split()
n = int(s[0])
score_l = int(s[1])
score_h = int(s[2])
l1, l2, l3, l4 = [], [], [], []


# 当某类考生中有多人总分相同时，按其德分降序排列；若德分也并列，则按准考证号的升序输出
def take_sum(info):
    return int(info[1]) + int(info[2]), int(info[1]), -int(info[0])


total = 0
for i in range(n):
    ss = input().split()  # split()的频繁使用导致超时
    num = int(ss[0])
    de = int(ss[1])
    cai = int(ss[2])

    if de >= score_l and cai >= score_l:
        if de >= score_h and cai >= score_h:
            l1.append(ss)
        elif de >= score_h:
            l2.append(ss)
        elif de >= cai:
            l3.append(ss)
        else:
            l4.append(ss)

print(len(l1 + l2 + l3 + l4))

for k in (l1, l2, l3, l4):
    k.sort(key=take_sum, reverse=True)
    for j in k:
        print(" ".join(str(i) for i in j))
# 两个测试点超时
