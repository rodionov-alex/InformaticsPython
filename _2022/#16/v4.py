def F(n):
    if n > 0:
        F(n - 3)
        F(n // 3)
        print(n)

F(9)