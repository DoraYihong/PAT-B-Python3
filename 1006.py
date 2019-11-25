num = input()
nums = []
for i in num:
    nums.append(int(i))
if len(nums) == 3:
    for i in range(nums[0]):
        print("B", end="")
    for i in range(nums[1]):
        print("S", end="")
    for i in range(nums[2]):
        print(str(i+1), end="")
elif len(nums) == 2:
    for i in range(nums[0]):
        print("S", end="")
    for i in range(nums[1]):
        print(str(i+1), end="")
else:
    for i in range(nums[0]):
        print(str(i+1), end="")
