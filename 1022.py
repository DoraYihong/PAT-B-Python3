a, b, d = list(map(float, input().split()))
c = a + b
result = []
if c == 0:
    print("0")
while c != 0:
    result.append(c % d)
    c = c // d
# print(result)
result.reverse()
# print(result)
print(''.join(str(int(i)) for i in result), end='')
