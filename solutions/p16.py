"""
2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2**1000?
"""


def sum_sq(num: int = 2, power: int = 1000):
    _sum = 0
    res_list = [int(i) for i in str(num**power)]

    return sum(res_list)


if __name__ == '__main__':
    print(sum_sq())
