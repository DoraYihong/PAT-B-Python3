str1 = list(input())
str2 = input()
for i in str2:
    while i in str1:
        str1.remove(i)

for i in range(len(str1)):
    if str1[i].islower:
        str1[i] = str1[i].upper()

str3 = []
for x in str1:
    if x not in str3:
        str3.append(x)
print(''.join(str3))
