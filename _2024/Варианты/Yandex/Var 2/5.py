for n in range(1000, 10000):
    nums = sorted(set(map(int, str(n))))

    if len(nums) == 4:
        r = int(''.join(map(str, sorted([nums[0] + nums[-1], nums[1] * nums[2]]))))

        if r > 85:
            print(n)
            break
