"""Простые делители числа 13195 - это 5, 7, 13 и 29.
Каков самый большой делитель числа 600851475143, являющийся простым числом?"""


def find_max_denominator(n: int):
    import math
    f = math.ceil(math.sqrt(n))

    for i in range(f, 3, -1):
        if n % i == 0:
            return i
    return None


print(find_max_denominator(600851475143))
