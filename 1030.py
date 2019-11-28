n, p = [int(i) for i in input().split()]
nums = sorted([int(i) for i in input().split()])
max_len = 0
for i in range(n):
    for j in range(i + max_len, n):
        if nums[j] > nums[i] * p:
            break
        max_len += 1
print(max_len)
# 嵌套循环易导致运行超时，简化处理
