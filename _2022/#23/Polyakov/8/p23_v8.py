def f(a, i, res):
    if i == 15:
        res.add(a)
    else:
        f(a + 2, i + 1, res)
        f(a * 2 + 1, i + 1, res)


results = set()
f(2, 0, results)

print(len(results))
