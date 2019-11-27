x = input().zfill(4)
num = []
if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
    print(x + " - " + x + " = 0000")
else:
    while True:
        num.clear()
        for i in range(4):
            num.append(int(x[i]))
        num.sort(reverse=True)
        digit1 = 1000 * num[0] + 100 * num[1] + 10 * num[2] + num[3]
        digit2 = 1000 * num[3] + 100 * num[2] + 10 * num[1] + num[0]
        diff = digit1 - digit2
        print(str(digit1).zfill(4)+" - "+str(digit2).zfill(4)+" = "+str(diff).zfill(4))
        x = str(diff).zfill(4)
        if diff == 6174:
            break
