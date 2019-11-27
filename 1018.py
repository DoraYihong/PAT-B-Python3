num = int(input())
win = lost = draw = 0
list1 = [0, 0, 0]  # 0B,1C,2J
list2 = [0, 0, 0]

for i in range(num):
    x = input().split()
    x1 = x[0]
    x2 = x[1]
    if x1 == x2:
        draw += 1
    elif x1 == 'C':
        if x2 == 'J':
            win += 1
            list1[1] += 1
        elif x2 == 'B':
            lost += 1
            list2[0] += 1
    elif x1 == 'J':
        if x2 == 'B':
            win += 1
            list1[2] += 1
        elif x2 == 'C':
            lost += 1
            list2[1] += 1
    elif x1 == 'B':
        if x2 == 'C':
            win += 1
            list1[0] += 1
        elif x2 == 'J':
            lost += 1
            list2[2] += 1

print(' '.join(str(i) for i in (win, draw, lost)))
print(' '.join(str(i) for i in (lost, draw, win)))

temp = list1.index(max(list1))
if temp == 0:
    print('B', end=" ")
if temp == 1:
    print('C', end=" ")
if temp == 2:
    print('J', end=" ")

temp = list2.index(max(list2))
if temp == 0:
    print('B', end="")
if temp == 1:
    print('C', end="")
if temp == 2:
    print('J', end="")
# 最后一个测试点超时
