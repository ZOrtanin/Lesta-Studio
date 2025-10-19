import time
import random


def merge_sort(arr):
    
    # Базовый случай: если массив состоит из одного элемента или пуст, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Разделяем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем обе половины
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Сливаем отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0

    # Сравниваем элементы из обеих половин и добавляем меньший в результат
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Добавляем оставшиеся элементы из левой половины (если есть)
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Добавляем оставшиеся элементы из правой половины (если есть)
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


if __name__ == "__main__":
    arr = [random.randint(0, 10_000_000) for _ in range(1_000_000)]

    print("Стандартная сортировка sorted(): ")
    start = time.time()
    sorted_arr = sorted(arr)
    end = time.time()
    print(f"Время сортировки: {end - start:.3f} сек")

    print("Cортировка методом слияния: ")
    start = time.time()
    sorted_arr = merge_sort(arr)
    end = time.time()
    print(f"Время сортировки: {end - start:.3f} сек")

