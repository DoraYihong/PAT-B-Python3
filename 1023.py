num = list(map(int, input().split()))
nums = []
for i in range(10):
    for j in range(num[i]):
        nums.append(i)
nums.sort()
if nums[0] == 0:
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[0] = nums[i]
            nums[i] = 0
            break
print(''.join(str(i) for i in nums), end="")
