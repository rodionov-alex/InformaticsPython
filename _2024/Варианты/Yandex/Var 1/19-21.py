def f(s1, s2, m, mistake=False):
    if s1 + s2 >= 231:
        return m % 2 == 0
    if m == 0:
        return 0

    h = [f(s1 + 4, s2, m - 1, mistake), f(s1 * 3, s2, m - 1, mistake),
         f(s1, s2 + 4, m - 1, mistake), f(s1, s2 * 3, m - 1, mistake)]

    return any(h) if (m - 1) % 2 == 0 else any(h) if mistake else all(h)


def minmax(lst):
    return min(lst), max(lst)


print('19)', min([s for s in range(1, 218) if f(10, s, 2, True)]))
print('20)', *[s for s in range(1, 218) if not f(10, s, 1) and f(10, s, 3)][:2])
print('21)', *minmax([s for s in range(1, 218) if not f(10, s, 2) and f(10, s, 4)]))
