x = input().split('E')
weishu, jiema = x[0], x[1]
sign = '' if weishu[0] == '+' else '-'
weishu = weishu[1:]
zhengshu, xiaoshu = weishu.split('.')
shu = zhengshu + xiaoshu
if float(jiema) == 0:
    print(sign + weishu)
elif jiema[0] == '+':
    temp = int(jiema) - len(xiaoshu)
    if temp >= 0:
        print(sign+shu+"0"*temp)
    else:
        print(sign+shu[:int(jiema)+1]+'.'+shu[int(jiema)+1:])
else:
    print(sign+"0."+"0"*(int(jiema[1:])-1)+shu)
