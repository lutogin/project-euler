"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.
Какое число является 10001-ым простым числом?
"""


def simple_in_number(limit):
    result = []
    import math

    for num in range(2, limit + 1):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            result.append(num)

    return result[-1]


print(simple_in_number(1001))
