print('-=-=-= РАБОТА С ФАЙЛАМИ =-=-=-')

# Прежде, чем начать работать с файлом, его надо открыть. Сделать это можно с помощью функции open().
# Поскольку файл содержит русские символы (кириллицу), то при открытии функции open() нужно указать
# кодировку, в которой ей надо читать файл.
f = open('text_file.txt', encoding='UTF-8')
# Таким образом переменная f теперь ассоциирована с нашим файлом и представляет собой поток для чтения
# или записи файла.

# Для того чтобы прочитать строку из файла, используется метод readline().



print('1 вызов f.readline():', f.readline())
print('2 вызов f.readline():', f.readline())
print('3 вызов f.readline():', f.readline())
f.close()
print()

with open('text_file.txt', encoding='UTF-8') as f:
    lines = f.readlines()
    print('lines = f.readlines() =>', lines)
    # lines = f.readlines() - повторный вызов readlines() результатов не даст т.к. файл уже прочитан
    lines = [x.strip() for x in lines]
    print(lines)

with open('data_file.txt') as f:
    print(f.readlines())

with open('data_file.txt') as f:
    data = []

    for s in f:
        data.append(int(s))

    print(data)

with open('data_file.txt') as f:
    data = [int(s) for s in f]
    print(data)

with open('data_file.txt') as f:
    data = list(map(int, f))
    print(data)
