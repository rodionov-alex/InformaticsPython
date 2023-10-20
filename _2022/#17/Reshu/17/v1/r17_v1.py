import math

f = open('17.txt')
nums = list(map(int, f.readlines()))
k = mx = 0

for i in range(len(nums) - 2):
    triple = sorted(nums[i:i + 3], reverse=True)
    a = triple[0]
    b = triple[1]
    c = triple[2]

    # Сумма двух коротких сторон должна быть больше длинной
    if a < b + c:
        # В треугольнике напротив самой длинной стороны лежит наибольший угол
        # Теорема косинусов: a^2 = b^2 + c^2 - 2 * b * c * cos(alf)
        cos_alf = (b * b + c * c - a * a) / (2 * b * c)
        alf = math.degrees(math.acos(cos_alf))

        # Если угол острый
        if alf < 90:
            k += 1
            mx = max(mx, sum(triple))

print(k, mx)