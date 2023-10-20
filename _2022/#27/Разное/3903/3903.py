with open('27-B.txt') as f:
    v = int(f.readline().split()[1])
    nums = list(map(int, f.readlines()))

    k = 0
    truck = 0

    while len(nums):
        while len(nums):
            truck = nums.pop(0)

            if truck > 0:
                break
        else:
            break

        i = 0

        while i < len(nums):
            value = nums[i]
            sumV = truck + value

            if sumV <= v:
                truck += value

                if truck < 0:
                    nums[i] = truck
                    truck = 0
                    i += 1
                else:
                    nums.pop(i)
            else:
                truck = v
                nums[i] = v - sumV
                i += 1


        k += 1

print(k)