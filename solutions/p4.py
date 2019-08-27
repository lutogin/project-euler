"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром,
полученное умножением двух двузначных чисел – 9009 = 91 × 99.
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
"""


def find_max_polindrom(max_num: int):

    def is_polindrom(n: int):
        _n = str(n)[::-1]
        return int(_n) == n

    min_num = max_num // 10

    res = [i*j for i in range(min_num, max_num) for j in range(min_num, i) if is_polindrom(i*j)]
    return max(res)


if __name__ == '__main__':
    print(find_max_polindrom(1000))
