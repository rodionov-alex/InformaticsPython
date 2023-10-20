import sys
sys.setrecursionlimit(100)

def f(n):
    if n <= 1:
        return n
    if n % 3 == 0:
        return n + f(n // 3)
    else:
        return n + f(n + 3)

n = 0
r = 0

while r <= 100:
    n += 1
    # Используем блок try для отлова ошибок, например таких как 'maximum recursion depth exceeded'
    try:
        r = f(n)
    # В случае возникновения ошибки
    except:
        pass  # Ничего не делать
    # Если ошибки не произошло
    else:
        # Проверяем r и выводим результат
        if r > 100:
            print(n)
