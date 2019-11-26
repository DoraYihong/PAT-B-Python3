import math

zhishu = []
x = input().split()
m = int(x[0])
n = int(x[1])
output = []


def prime(num):
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


zhishu.append(2)
for i in range(3, 11 * n, 2):
    if prime(i):
        zhishu.append(i)

for i in range(m - 1, n):
    output.append(str(zhishu[i]))

for i in range(1, len(output)):
    if i % 10 == 0:
        print(output[i - 1])
    else:
        print(output[i - 1], end=" ")
print(output[len(output) - 1], end="")
