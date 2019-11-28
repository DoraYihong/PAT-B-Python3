x = input().split()
n = int(x[0])
sign = x[1]

temp = (n + 1) / 2
amount = 0
i = 1
while amount <= temp:
    amount += i
    i += 2
total = i - 4
if n in range(8, 17):
    total = 3

y = n
for i in range(1, total + 1, 2):
    y -= 2 * i
remaining = y + 1

for i in range(total, 0, -2):
    print(" " * int((total - i) / 2) + sign * i)
for i in range(1, total + 1, 2):
    if i != 1:
        print(" " * int((total - i) / 2) + sign * i)
print(remaining)
# 神奇地通过了所有测试点
