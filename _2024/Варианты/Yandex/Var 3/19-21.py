def minmax(lst):
    return min(lst), max(lst)

def f(s1, s2, m, mistake=False):
    if s1 + s2 >= 189:
        return m % 2 == 0
    if m == 0:
        return 0
    h = (f(s1, s2 + s1, m - 1, mistake),
         f(s1 + s2, s2, m - 1, mistake),
         f(max(s1, s2), max(s1, s2), m - 1, mistake))
    return any(h) if (m - 1) % 2 == 0 else any(h) if mistake else all(h)

print('19)', min([s for s in range(1, 184) if f(5, s, 2, True)]))
print('20)', *minmax([s for s in range(1, 184) if not f(5, s, 1) and f(5, s, 3)]))
print('21)', min([s for s in range(1, 184) if not f(5, s, 2) and f(5, s, 4)]))
