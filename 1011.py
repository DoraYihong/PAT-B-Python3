t = int(input())
a = []
b = []
c = []
flag = []

for i in range(t):
    x = input().split()
    a.append(int(x[0]))
    b.append(int(x[1]))
    c.append(int(x[2]))

for i in range(t):
    if a[i] + b[i] > c[i]:
        flag.append(True)
    else:
        flag.append(False)

for i in range(t):
    if flag[i]:
        print("Case #" + str(i + 1) + ": true")
    else:
        print("Case #" + str(i + 1) + ": false")
