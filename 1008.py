def move(a):
    temp = a[n - 1]
    for i in range(n - 1, 0, -1):
        y[i] = y[i - 1]
    a[0] = temp
    return a


x = input().split()
y = input().split()
z = []
for i in y:
    z.append(int(i))
y = z

n = int(x[0])
m = int(x[1])

for i in range(m):
    y = move(y)
print(" ".join(str(i) for i in y))
