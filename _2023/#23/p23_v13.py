def f(a, b, chet):
    if a > b or chet > 3:
        return 0
    if a == b:
        return 1
    a1 = a + 2
    a2 = a * 2
    a3 = a * 3
    return f(a1, b, chet + (a1 % 2 == 0)) + f(a2, b, chet + (a2 % 2 == 0)) + f(a3, b, chet + (a3 % 2 == 0))

print(f(1, 402, 0))

