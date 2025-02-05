print('-=-=-= ИСКЛЮЧЕНИЯ =-=-=-')
# Исключения (exceptions) - ещё один тип данных в python. Исключения необходимы для того, чтобы сообщать
# программисту об ошибках. Самый простой пример исключения - деление на ноль. В данном примере, если
# попытаться поделить a на b то интерпретатор выдас нам ошибку ZeroDivisionError.

a = 5
b = 0
# print(a / b)  # ошибка ZeroDivisionError

# Чтобы избежать прерывания программы в подобных ситуациях - исключения следует обрабатывать при помощи
# блока try - except.

# В блок try пишется код в котором может возникнуть исключение
try:
    print(a / b)
# Если возникла ошибка ZeroDivisionError, то управление передается в этот блок except
except ZeroDivisionError:
    print('Ошибка ZeroDivisionError')

print('конец программы')
print()

# Как можно заметить, при возникновении исключения наша программа не прерывается, а управление предается
# в блок excep, где происходит обработка исключения, после чего выполнение программы продолжается.

# Если в блоке excep не указывать тип исключения, тогда он обудет ловить и обрабатывать все исключения,
# для которых не написан отдельный блок except.

try:
    c = [1, 2, 3]
    print(c[5])  # исключение - индекс не входит в диапазон элементов.
except ZeroDivisionError:
    print('Ошибка ZeroDivisionError')
except:
    print('Все остальные ошибки')

print('конец программы')
print()

# В данном примере нет блока except для исключения IndexError, поэтому обработка исключения будет произведена
# в "пустом" блоке except.

try:
    c = [1, 2, 3]
    print(c[5])
    print(a / b)
except ZeroDivisionError:
    print('Ошибка ZeroDivisionError')
except IndexError:
    print('Ошибка IndexError')
except:
    print('Все остальные ошибки')

print('конец программы')
print()

# Обратите внимание, что в данном примере есть 2 исключения: IndexError и ZeroDivisionError. Но, при выполнении
# программы, обработано из них будет только одно - то что встретится раньше. После получения исключения в блоке
# try его выполнение прерывается, и управление передается в блок except.


print('-=-=-= БЛОКИ ELSE И FINALLY =-=-=-')
# Помимо блока excep, который обрабатывается исключения, существует еще 2 блока: else и finally. Блок else
# выполняется в том случае, если при выполнении кода в блоке try не воникало никаких исключений. А блок
# finally вызывается всегда, вне зависимости от того, возникало ли исключение или нет.

try:
    c = [1, 2, 3]
    print(c[2])
    print(b / a)
except ZeroDivisionError:
    print('Ошибка ZeroDivisionError')
except IndexError:
    print('Ошибка IndexError')
except:
    print('Все остальные ошибки')
# Если ошибок не возникало, то управление передается в блок else
else:
    print('Ошибок нет')
# Блок finally выполняется вне зависимости от того, были ошибки или нет
finally:
    print('finally')

print('конец программы')

# Блоки обработки исключений try-except должны идти в следующем порядке:
# try: - в начале пишется блок try и в нем код в котором могут возникнуть исключения
# except SomeError: - затем идут блоки except с указанием типов исключений
# except: - далее идет "пустой" блок except для обработки всех исключений
# else: - предпоследним идет else
# finally: - и последним идет блок finally


# Далее описана иерархия основных встроенных в python исключений:

# BaseException - базовое исключение, от которого берут начало все остальные.
#   SystemExit - исключение, порождаемое функцией sys.exit при выходе из программы.
#   KeyboardInterrupt - порождается при прерывании программы пользователем (обычно сочетанием клавиш Ctrl+C).
#   GeneratorExit - порождается при вызове метода close объекта generator.
#   Exception - а вот тут уже заканчиваются полностью системные исключения и начинаются обыкновенные, с которыми
#               можно работать.
#       StopIteration - порождается встроенной функцией next, если в итераторе больше нет элементов.
#       ArithmeticError - арифметическая ошибка.
#           FloatingPointError - порождается при неудачном выполнении операции с плавающей запятой. На практике
#                                встречается нечасто.
#           OverflowError - возникает, когда результат арифметической операции слишком велик для представления.
#                           Не появляется при обычной работе с целыми числами (так как python поддерживает длинные
#                           числа), но может возникать в некоторых других случаях.
#           ZeroDivisionError - деление на ноль.
#       AssertionError - выражение в функции assert ложно.
#       AttributeError - объект не имеет данного атрибута (значения или метода).
#       BufferError - операция, связанная с буфером, не может быть выполнена.
#       EOFError - функция наткнулась на конец файла и не смогла прочитать то, что хотела.
#       ImportError - не удалось импортирование модуля или его атрибута.
#       LookupError - некорректный индекс или ключ.
#           IndexError - индекс не входит в диапазон элементов.
#           KeyError - несуществующий ключ (в словаре, множестве или другом объекте).
#       MemoryError - недостаточно памяти.
#       NameError - не найдено переменной с таким именем.
#           UnboundLocalError - сделана ссылка на локальную переменную в функции, но переменная не определена ранее.
#       OSError - ошибка, связанная с системой.
#           BlockingIOError
#           ChildProcessError - неудача при операции с дочерним процессом.
#           ConnectionError - базовый класс для исключений, связанных с подключениями.
#               BrokenPipeError
#               ConnectionAbortedError
#               ConnectionRefusedError
#               ConnectionResetError
#           FileExistsError - попытка создания файла или директории, которая уже существует.
#           FileNotFoundError - файл или директория не существует.
#           InterruptedError - системный вызов прерван входящим сигналом.
#           IsADirectoryError - ожидался файл, но это директория.
#           NotADirectoryError - ожидалась директория, но это файл.
#           PermissionError - не хватает прав доступа.
#           ProcessLookupError - указанного процесса не существует.
#           TimeoutError - закончилось время ожидания.
#       ReferenceError - попытка доступа к атрибуту со слабой ссылкой.
#       RuntimeError - возникает, когда исключение не попадает ни под одну из других категорий.
#       NotImplementedError - возникает, когда абстрактные методы класса требуют переопределения в дочерних классах.
#       SyntaxError - синтаксическая ошибка.
#           IndentationError - неправильные отступы.
#               TabError - смешивание в отступах табуляции и пробелов.
#       SystemError - внутренняя ошибка.
#       TypeError - операция применена к объекту несоответствующего типа.
#       ValueError - функция получает аргумент правильного типа, но некорректного значения.
#       UnicodeError - ошибка, связанная с кодированием / раскодированием unicode в строках.
#           UnicodeEncodeError - исключение, связанное с кодированием unicode.
#           UnicodeDecodeError - исключение, связанное с декодированием unicode.
#           UnicodeTranslateError - исключение, связанное с переводом unicode.
#       Warning - предупреждение.
