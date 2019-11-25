num = int(input())
numList = []

i = 1
while i <= num:
    numList.append(input())
    i += 1

i = 0
while i < num:
    num_A_left = 0
    num_A_mid = 0
    num_A_right = 0
    flag_t = False
    flag_p = False
    judge = True
    for letter in numList[i]:
        # 不能没有P，P和T的个数都只有一个
        if letter != "P" and letter != "A" and letter != "T":
            judge = False
            break
        if letter == "A" and flag_p is not True and flag_t is not True:
            num_A_left += 1
        if letter == "A" and flag_p is True and flag_t is not True:
            num_A_mid += 1
        if letter == "A" and flag_p is True and flag_t is True:
            num_A_right += 1
        if letter == "P" and flag_p is True:
            judge = False
            break
        if letter == "T" and flag_t is True:
            judge = False
            break
        if letter == "P":
            flag_p = True
        if letter == "T":
            flag_t = True
    # PT之间不能没有A，左边A数*中间A数应等于右边A数，不能没有T
    if judge is False or num_A_mid == 0 or num_A_left*num_A_mid != num_A_right or flag_t is False:
        print("NO")
    else:
        print("YES")
    i += 1
