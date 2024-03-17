"""
Функция для извлечения данных:
Возвращает: дата(год, месяц, день), время(час, минута, секунда), номер программиста, номер задания
"""
def getData(s: str):
    sDateTime, nProger, nTask = s.split()
    sDate, sTime = sDateTime.split('T')
    return tuple(map(int, sDate.split('-'))), tuple(map(int, sTime.split(':'))), int(nProger), int(nTask)

with open('26.txt') as f:
    # распаковка исходных данных
    source_data = [getData(x) for x in f.readlines()[1:]]
    # Сортировка исходных данных по дате и времени
    source_data.sort(key=lambda x: (x[0], x[1]))
    # Словарь программистов
    # ключ: номер программиста, значение: количество решенных задач, дата и время последней задачи
    progers = {}
    # Перебор исходных данных и заполнение словаря программистов
    for date, time, nProger, nTask in source_data:
        if nProger in progers.keys():
            # Увеличить количество решенных задач на 1 и обновить время решения посленей задачи
            progers[nProger] = (progers[nProger][0] + 1, date, time)
        else:
            # Новый программист, решил 1 задачу, ее дата и время
            progers[nProger] = (1, date, time)

    # Максимальное количество решенных задач
    max_tasks = progers[max(progers, key=progers.get)][0]
    # Список программистов, решивших максимальное количество задач
    mxTaskSloved = []
    # Заполнение списка: номер программиста, дата и время решения последней задачи
    for p in progers:
        if progers[p][0] == max_tasks:
            taskCount, date, time = progers[p]
            mxTaskSloved.append((p, date, time))
    # Сортировка списка по дате и времени
    mxTaskSloved.sort(key=lambda x: (x[1], x[2]))
    # Вывод результата
    print(max_tasks, mxTaskSloved[0][0], sep='\t')
