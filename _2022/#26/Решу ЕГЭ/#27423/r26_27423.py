f = open('26.txt')
space, n = f.readline().split()
space, n = int(space), int(n)
nums = []

for _ in range(n):
    nums.append(int(f.readline()))

f.close()
nums.sort()

count = 0
l = len(nums)
size = 0

while size <= space and count < l:
    size += nums[count]
    count += 1

size -= nums[count] + nums[count - 1]
leftSpace = space - size
j = count
count -= 1

while nums[j] <= leftSpace and j < l:
    j += 1


print(count, nums[j - 1])
