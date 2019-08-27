"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.
"""


def simple_number_sum(limit: int = 2000000) -> int:
    result = []
    import math

    for num in range(2, limit):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            result.append(num)

    return sum(result)


if __name__ == '__main__':
    print(simple_number_sum(2000000))
