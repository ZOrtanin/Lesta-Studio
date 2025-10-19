import unittest
from question2 import ListQueue, LinkedListQueue  # Предполагаем, что реализация в файле list_queue.py


class TestQueue(unittest.TestCase):
    def setUp(self):
        """Создаём пустую очередь перед каждым тестом."""
        test_method = getattr(self, self._testMethodName)
        print(f"\n--- Тест: {self._testMethodName} ---")
        print(f"{test_method.__doc__}")
        self.queue = ListQueue()

    def test_enqueue_and_dequeue(self):
        """Тест: добавление и удаление элементов."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)

        self.assertEqual(self.queue.dequeue(), 1)  # Первый пришёл — первый ушёл
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)

    def test_dequeue_from_empty(self):
        """Тест: попытка удаления из пустой очереди."""
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_peek(self): 
        """Тест: просмотр первого элемента без удаления."""

        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.peek(), 10)  # Первый элемент — 10
        self.assertEqual(self.queue.size(), 2)    # Размер не изменился

    def test_peek_empty(self):
        """Тест: просмотр пустой очереди."""
        with self.assertRaises(IndexError):
            self.queue.peek()

    def test_is_empty(self):
        """Тест: проверка пустоты очереди."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_size(self):
        """Тест: проверка размера очереди."""
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.queue.dequeue()
        self.assertEqual(self.queue.size(), 1)

    def test_enqueue_dequeue_order(self):
        """Тест: порядок элементов (FIFO)."""
        test_data = [5, 3, 7, 1]
        for item in test_data:
            self.queue.enqueue(item)

        # Проверяем, что элементы выходят в том же порядке
        for expected_item in test_data:
            self.assertEqual(self.queue.dequeue(), expected_item)

    def test_mixed_operations(self):
        """Тест: чередование enqueue и dequeue."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertTrue(self.queue.is_empty())

    def test_large_queue(self):
        """Тест: работа с большой очередью (10 000 элементов)."""
        for i in range(10000):
            self.queue.enqueue(i)
        for i in range(10000):
            self.assertEqual(self.queue.dequeue(), i)
        self.assertTrue(self.queue.is_empty())


def run_tests(queue_class, name):
    """ Динамически создаём класс для тестирования конкретной реализации """
    class TestQueueImplementation(TestQueue):
        def setUp(self):
            """ Создаём пустую очередь перед каждым тестом. """
            test_method = getattr(self, self._testMethodName)
            print(f"\n--- Тест: {self._testMethodName} ---")
            print(f"{test_method.__doc__}")
            self.queue = queue_class()

    # Собираем все тесты из TestQueueImplementation
    suite = unittest.TestLoader().loadTestsFromTestCase(TestQueueImplementation)
    # Запускаем тесты
    print(f" ----- {name} ----- ")
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    run_tests(ListQueue, "Очередь из списка")
    run_tests(LinkedListQueue, "Очередь из связного списка")
