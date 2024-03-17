def f(a, b):
    if a > b or a == 25:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a * 2, b) + f(a * 5, b)

print(f(5, 115))
