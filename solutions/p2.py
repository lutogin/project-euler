"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2,
первые 10 элементов будут: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""


def summ_even_fibo(max_val: int) -> int:
    a, b = 1, 1
    e_fi = []

    while a < max_val:
        if a % 2 == 0:
            e_fi.append(a)

        a, b = b, a+b

    return sum(e_fi)


if __name__ == '__main__':
    print(summ_even_fibo(4000000))
