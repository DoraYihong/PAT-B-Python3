nums = input().split()
num = []
for i in nums:
    num.append(int(i))
nums = num
result = []
for i in range(0, len(nums), 2):
    if nums[i] * nums[i+1] != 0:
        result.append(nums[i] * nums[i + 1])
        result.append(nums[i + 1] - 1)
if len(result) != 0:
    print(" ".join(str(i) for i in result))
else:
    print("0 0")
