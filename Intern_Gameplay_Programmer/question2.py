class ListQueue:
    """ Реализация очереди по принцепу FIFO-очередь на списке"""

    def __init__(self):
        """ Создание очереди """
        self.queue = []

    def enqueue(self, item) -> None:
        """ Добовляем в конец очереди """
        self.queue.append(item)

    def dequeue(self) -> int:
        """ Берем с начала очереди не эфективная функция O(n)"""
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.queue.pop(0)

    def peek(self) -> int:
        """ Смотрим что в начале очереди """
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self.queue[0]

    def clear_queue(self) -> None:
        """ Отчищаем очередь """
        self.queue.clear()

    def size(self) -> int:
        """ Смотрим размер очереди """
        return len(self.queue)

    def is_empty(self) -> bool:
        """ Обрабатываем пустоту очереди """
        return len(self.queue) == 0 

# Связанный список
class Box:  
    """ Узел связанного списка """
    def __init__(self, cat=None):    
        self.cat = cat    
        self.nextcat = None


class LinkedListQueue:
    """ FIFO-очередь на связном списке """  
    def __init__(self):
        """ Инициализируем очередь """    
        self.head = None
        self.tail = None
        self._size = 0

    def enqueue(self, newcat):
        """ Добовление узла в конец списка """    
        newbox = Box(newcat)    
        
        if self.head is None:      
            self.head = newbox      
            self.tail = newbox
        else:
            self.tail.nextcat = newbox
            self.tail = newbox
        self._size += 1

    def dequeue(self):
        """ 
        Удаляет и возвращает первый элемент очереди что 
        более эффективно O(1) чем в очереди на списке 
        """
        if self.head is None:
            raise IndexError(" Очередь пуста ")

        item = self.head.cat
        self.head = self.head.nextcat

        if self.head is None:
            self.tail = None

        self._size -= 1
        
        return item

    def peek(self):
        """ Берем первый элемент из очереди """
        if self.head is None:
            raise IndexError(" Очередь пуста ")
        return self.head.cat

    def clear_queue(self):
        """ Отчищаем очередь O(1)"""
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self):
        """ Смотрим пустая ли очередь """
        return self.head is None

    def size(self):
        """ Смотрим размер очереди """
        return self._size 