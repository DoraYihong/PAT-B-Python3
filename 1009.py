words = input().split()
new = []
for i in range(len(words)-1, -1, -1):
    new.append(words[i])
print(" ".join(new))
