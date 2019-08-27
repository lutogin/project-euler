"""
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a2 + b2 = c2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""


def pifagor_trio(limit_p: int = 1000) -> list or None:
    for z in range(limit_p):
        for y in range(z):
            for x in range(y):
                if x**2 + y**2 == z**2 and x + y + z == 1000:
                    return [x, y, z]

    return None


if __name__ == '__main__':
    print(pifagor_trio())
