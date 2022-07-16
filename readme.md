Данное задание призвано оценить работу с Python, уровень владения культурой программирования, а также показать пример того, с чем придется столкнуться в работе. Несмотря на это, данные в задании имеют очень упрощенную схему относительно реальных.

Задание:

1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.

# Вариант 1

                def isEven(value):
                    return value%2==0

плюсы -

минусы -

# Вариант 2

                def myEven(value):
                    
                    while True:                        
                        value = value - 2                        
                        if value==0:
                            return True
                        elif value<2:
                            return False

плюсы -

минусы -


2. На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. Объяснить плюсы и минусы каждой реализации.

3. На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком чисел (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.