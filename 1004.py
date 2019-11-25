num = int(input())
name = []
sid = []
mark = []
for i in range(num):
    s = input()
    x = s.split(" ", 2)
    name.append(x[0])
    sid.append(x[1])
    mark.append(int(x[2]))  # 注意把字符串转化为数字处理
i = mark.index(max(mark))
print(name[i]+" "+sid[i])
i = mark.index(min(mark))
print(name[i]+" "+sid[i])
