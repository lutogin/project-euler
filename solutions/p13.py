"""
Найдите первые десять цифр суммы следующих ста 50-значных чисел.
"""


def i_sum(num_limit: int = 10):
    with open('p13.txt', 'r') as file:
        data = file.read()

    return str(sum((map(lambda x: int(x), data.split()))))[:num_limit]


if __name__ == '__main__':
    print(i_sum())
