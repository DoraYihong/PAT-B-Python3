nums = input().split()
num = []
for i in range(1, len(nums)):
    num.append(int(nums[i]))
nums = num

a1 = []
a2 = []
a3 = []
a4 = []
a5 = []

for i in nums:
    if i % 10 == 0:
        a1.append(i)
    elif i % 5 == 1:
        a2.append(i)
    elif i % 5 == 2:
        a3.append(i)
    elif i % 5 == 3:
        a4.append(i)
    elif i % 5 == 4:
        a5.append(i)

if len(a1) == 0:
    print("N", end=" ")
else:
    print(sum(a1), end=" ")

if len(a2) == 0:
    print("N", end=" ")
else:
    total = a2[0]
    for i in range(1, len(a2)):
        if i % 2 == 1:
            total -= a2[i]
        else:
            total += a2[i]
    print(total, end=" ")

if len(a3) == 0:
    print("N", end=" ")
else:
    print(len(a3), end=" ")

if len(a4) == 0 or len(a4) == 1:
    print("N", end=" ")
else:
    temp = sum(a4)/len(a4)
    temp = round(temp, 1)
    print(temp, end=" ")

if len(a5) == 0:
    print("N", end="")
else:
    print(max(a5), end="")
