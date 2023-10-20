# Автор: Л. Шастин

with  open('26-86.txt') as F:
  N = int(F.readline())
  data = sorted(list(map(int, x.split())) for x in open('26-86.txt') if ' ' in x)
  print(data)

  k = {x[1]: [y[0] for y in data if y[1] == x[1]] for x in data}
  print(k)
# day = [0]*(60*16 + 1)
# times = []
# for p, t in k.items():
#     if len(t) > 1: times += [(sum([t[i] - t[i - 1] for i in range(len(t)) if i%2])/(len(t) - len(t)%2), p)]
#     for i in range(1, len(t), 2):
#         day[t[i]] += 1
#
# print(max([sum(day[s:s + 60]) for s in range(60*16 + 1)]), sorted(times)[-1][1])

