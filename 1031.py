num = int(input())
weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
sign = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
num_list = []
for i in range(num):
    enter = input()
    if not enter[0:16].isdigit():
        num_list.append(enter)
        continue
    total = 0
    for j in range(17):
        total += weights[j] * int(enter[j])
    if sign[total % 11] != enter[17]:
        num_list.append(enter)
if len(num_list) == 0:
    print("All passed")
else:
    for i in num_list:
        print(i)
