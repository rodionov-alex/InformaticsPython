s = int(input())
n = 127
while s - n > 0:
  s = s + 15
  n = n + 20
print(s)