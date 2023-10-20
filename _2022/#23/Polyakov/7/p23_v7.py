def f(a, i, res):
    if i == 11:
        res.add(a)
    else:
        f(a + 1, i + 1, res)
        f(a * 2 + 1, i + 1, res)


results = set()
f(3, 0, results)

print(len(results))
