n = input()
sum = 0
shuzi = ["ling", "yi", "er", "san", "si", "wu", "liu", "qi", "ba", "jiu"]
out = []

# 注意：如果自然数n是int数据类型，则容易溢出
for num in n:
    sum += int(num)

for num in str(sum):
    out.append(int(num))

i = len(out) - 1
j = 0
while (j < i):
    print(shuzi[out[j]]+" ", end="")
    j += 1
print(shuzi[int(out[i])], end="")
