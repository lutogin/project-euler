"""
n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!.
"""


def summary_factorial(limit: int = 100) -> int:
    factorial = 1
    for i in range(limit, 0, -1):
        factorial *= i

    f_list = [int(e) for e in str(factorial)]

    return sum(f_list)


if __name__ == '__main__':
    print(summary_factorial())
