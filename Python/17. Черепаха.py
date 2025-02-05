import turtle

# НАЧАЛО РАБОТЫ С ЧЕРЕПАХОЙ

# Перед началом работы с черепахой рекомендуется задать следующие параметры: масштаб, размер окна, скорость черепахи.
scale = 30                          # переменная которая будет отвечать за масштаб рисования
turtle.getscreen().xscale = scale   # задать масштаб по X
turtle.getscreen().yscale = scale   # задать масштаб по Y
turtle.setup(1.0, 1.0)              # установить ширину и высоту окна
# Вещественная 1.0 означает, что ширина и высота окна задается в пропорциях экрана 1 к 1;
# так же можно задавать размер в пикселях если использовать целочисленные аргументы.

# Задать скорость анимации черепахи
turtle.speed(10)

# Так же, хоть и не обязательно, но есть возможность поменять цвет фона и черепахи:
turtle.getscreen().bgcolor("black")     # Задать цвет фона окна
turtle.color("cyan")                    # Задать цвет черепахи и лиинй

# Данный метод позволяет пропустить анимацию черепахи и получить сразу результат. В конце необходимо
# будет вызвать метод update().
# turtle.tracer(0)

# По умолчанию в питоне черепаха смотрит вдоль положительного направления оси абсцисс (X). Это следует
# учитывать если в условии задачи черепаха должна быть направлена вдоль положительного направления оси ординат (Y).


# ОСНОВНЫЕ ФУНКЦИИ ЧЕРЕПАХИ

turtle.up()             # Поднять хвост черепахи
turtle.down()           # Опустить хвост черепахи
turtle.isdown()         # Узнать, опущен ли хвост у черепахи

turtle.left(90)         # Повернуть черепаху налево на 90 градусов
turtle.lt(90)           # Короткое название функции поворота налево
turtle.right(90)        # Повернуть черепаху направо на 90 градусов
turtle.rt(90)           # Короткое название функции поворота направо

turtle.forward(10)      # Переместить черепаху вперед на расстояние 10
turtle.fd(10)           # Короткое название функции перемещения вперед
turtle.backward(10)     # Переместить черепаху назад на расстояние 10
turtle.back(10)         # Короткое название функции перемещения назад
turtle.bk(10)           # Самок короткое название функции перемещения назад

turtle.home()           # Вернуть черепаху в начальную позицию (0, 0)
turtle.goto(10, 10)     # Перемещает черепаху по координатам (x, y)
turtle.dot(5, 'red')    # Поставить точку цвета 'red' диаметром 5

turtle.position()       # Возвращает кортеж с текущими координатами черепахи
turtle.pos()            # Коротное название функции текущих координат черепахи


# ДОПОЛНИТЬЕЛЬНЫЕ ФУНКЦИИ ЧЕРЕПАХИ, КОТОРЫЕ МОГУТ ПРИГОДИТЬСЯ

turtle.hideturtle()     # Скрыть черепаху
turtle.showturtle()     # Показать черепаху
turtle.ht()             # Коротное название функции "Скрыть черепаху"
turtle.st()             # Коротное название функции "Показать черепаху"
turtle.isvisible()      # Узнать, видна ли черепаха

turtle.pensize(3)       # Ширина следа, оставляемого черепахой
turtle.distance(5, 5)   # Возвращает расстояние от текущего расположения черепахи до точки с координатами (x, y)


# ЗАВЕРШЕНИЕ РАБОТЫ С ЧЕРЕПАХОЙ

# По завершению работы с черепахой, если параметр tracer был задан нулем, необходимо вызвать функцию
# update() чтобы перерисовать содержимое окна.
turtle.update()

# Функция done() означает конец работы черепахи и предотвращает закрытие окна после ее работы.
turtle.done()

# Функция exitonclick() тоже позволяет предотвратить закрытие окна после работы черепахи, но
# закроет его при первом клике мышью.
turtle.exitonclick()
