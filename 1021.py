n = input()
count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
for i in range(len(n)):
    count[int(n[i])] += 1
for i in range(10):
    if count[int(i)] != 0:
        print(str(i)+":"+str(count[int(i)]))
