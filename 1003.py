num = int(input())
numList = []

i = 1
while i <= num:
    numList.append(input())
    i += 1

i = 0
while i < num:
    for letter in numList[i]:
        if letter != "P" and letter != "A" and letter != "T":
            print("NO")
            break
    i += 1
