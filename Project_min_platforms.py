# id посылки: 129034224
from typing import List


def min_platforms(weights: List[int], limit: int) -> int:
    # Сортируем массив весов роботов
    weights.sort()
    left, right = 0, len(weights) - 1
    platforms = 0

    while left <= right:
        # Если два робота помещаются на одну платформу
        if weights[left] + weights[right] <= limit:
            left += 1  # Легкий робот отправляется
        # Тяжелый робот всегда отправляется
        right -= 1
        platforms += 1

    return platforms


if __name__ == "_main_":
    # Ввод данных
    with open("input.txt", "r") as file:
        weights = list(map(int, file.readline().strip().split()))
        limit = int(file.readline().strip())

    # Вычисляем минимальное количество платформ
    result = min_platforms(weights, limit)

    # Запись результата в файл
    with open("output.txt", "w") as file:
        file.write(str(result))
