def f(a, b, oper: list):
    if a > b:
        return 0
    if a == b:
        return oper[0] <= 4 and oper[1] >= 2 and oper[2] == 5

    a1 = a * 5
    a2 = a * 3
    a3 = a + 45

    op1 = oper.copy()
    op2 = oper.copy()
    op3 = oper.copy()
    op1[0] += 1
    op2[1] += 1
    op3[2] += 1

    return f(a1, b, op1) + f(a2, b, op2) + f(a3, b, op3)


print(f(1, 2970, [0, 0, 0]))
