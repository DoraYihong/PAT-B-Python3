import math


def prime(num):
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


primeList = [2]
n = int(input())
for i in range(3, n+1, 2):
    if prime(i) is True:
        primeList.append(i)

count = 0
for i in range(len(primeList) - 1):
    if primeList[i + 1] - primeList[i] == 2:
        count += 1
print(count)
