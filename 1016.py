x = input().split()
a, da, b, db = x[0], x[1], x[2], x[3]
pa, pb, pat, pbt = 0, 0, 0, 0

for i in a:
    if i == da:
        pat += 1

for i in b:
    if i == db:
        pbt += 1

temp = 0.1
for i in range(pat):
    temp *= 10
    pa += temp * int(da)

temp = 0.1
for i in range(pbt):
    temp *= 10
    pb += temp * int(db)

print(int(pa+pb))
