def F(n):
    print(n)
    if n < 5:
        F(n + 1)
        F(n + 3)

F(1)